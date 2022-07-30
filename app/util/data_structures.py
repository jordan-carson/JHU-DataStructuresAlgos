class Node:
    def __init__(self, data, next_element=None):
        self.data = data
        self.next = next_element

    def __repr__(self):
        return self.data


class CircularNode:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def is_empty(self):
        return True if self.size == 0 else False

    def insert_index(self, data, index):
        if index < 0 or index > self.size:
            raise Exception("Index is out of bounds...")
        else:
            new_node = Node(data)
            self.size += 1

            if index == 0:
                # new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
            else:
                list_node = self.get_list_node(index - 1)
                new_node.next = list_node.next
                list_node.next = new_node

    def insert(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        new_node = Node(data)
        # traverse till the last node
        tmp = self.head

        while tmp is not None:
            tmp = tmp.next

        tmp.next = new_node
        return

    @staticmethod
    def insert_nth(head, data, pos: int):
        if head is None or pos == 0:
            return Node(data)
        else:
            next_node = head
            while pos > 1:
                next_node = next_node.next
                pos -= 1

            next_node.next = Node(data, next_node.next)
        return head

    def remove(self, index):
        # tmp: Node
        if index < 0 or index > self.size:
            raise Exception("Index is out of bounds...")
        else:
            if index == 0:
                tmp = self.head
                self.head = tmp.next
            else:
                list_node = self.get_list_node(index - 1)
                tmp = list_node.next
                list_node.next = tmp.next

        self.size -= 1
        tmp.next = None
        return tmp.data

    def get_list_node(self, index):
        if index < 0 or index > self.size or self.size == 0:
            raise Exception("Index is out of bounds")

        tmp = self.head

        while tmp is not None:
            tmp = tmp.next

        # for i in range(0, index):
        #     tmp = tmp.next
        #
        return tmp

    def to_string(self):
        raise NotImplementedError


class DequeDLL:
    """
    Double Linked List with header + circular as Deque.
    """
    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    def print_change(self):
        print(f'Current DoubleLinkedList Length={self.length} Head={self.head} Rear={self.rear}.')

    def insert_left(self, item_data):
        if self.head is None:
            new_node = Node(item_data)
            self.head = new_node
            return

        # else, create a new node and init with the item's data
        new = Node(item_data)
        self.head.left = new
        new.right = self.head

        # ensure to point head at the new node
        self.head = new

        self.length += 1
        self.print_change()
        return

    def delete_right(self):
        if self.head is None:
            return # the list has nothing to delete

        if self.head.right is None:
            self.head = None
            return

        # if were here the head is not none and head.read is not None
        node = self.head
        # loop until right is not none
        while node.right is not None:
            node = node.right
        val = node.value
        node.left.right = None
        node.right = None
        print(f'Item {val} has been removed from {__class__.__name__}')

        self.length -= 1
        self.print_change()
        return

    def insert_right(self, item_data):
        new = Node(item_data)
        head = self.head

        while head.right is not None:
            head = head.right

        head.right = new
        new.left = head
        self.length += 1
        self.print_change()
        return

    def delete_left(self):
        if self.head is None:
            return

        val = self.head.value
        self.head.left = None
        self.rear.right = self.head.right
        self.head.right = None
        self.head = self.rear.right
        self.head.left = self.rear
        print(f'Item {val} has been removed from {__class__.__name__}')

        self.length -= 1
        self.print_change()
        return
