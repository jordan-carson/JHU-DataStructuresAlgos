
class AntiNode:
    def __init__(self):
        self.item = None
        self.right = None
        self.left = None


class NonCircularDeque:
    def __init__(self):
        self.current_node = None

    def insert_left(self, item):
        curr_node = self.current_node

        if curr_node is None:
            new_node = AntiNode()
            new_node.item = item
            new_node.left = None
            new_node.right = None
            return

        else:
            while curr_node.left is not None:
                curr_node = curr_node.left

            curr_node.left = AntiNode()
            curr_node.left.item = item
            curr_node.left.left = None
            curr_node.left.right = curr_node

            return

    def delete_right(self):
        curr_node = self.current_node
        if curr_node is None:
            return None
        else:
            while curr_node.right is not None:
                curr_node = curr_node.right

            item = curr_node.item
            curr_node = curr_node.left
            curr_node.right.left = None
            curr_node.right = None
            return item


class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


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


class KStackQueue:

    def __init__(self, nbr_queues, array_length):
        self.nbr_queues = nbr_queues
        self.array_length = array_length
        self.array = [-1] * array_length
        self.front = [-1] * array_length
        self.rear = [-1] * array_length
        self.next = list(range(1, array_length)).append(-1)
        self.free = 0

    def isEmpty(self, qnbr):
        if self.front[qnbr] == -1:
            return True
        return False

    def isFull(self, qnbr):
        if self.free == -1:
            return True
        return False

    def enqueue(self, item, qnbr):
        if self.isFull(qnbr):
            return
        next_free = self.next[self.free]
        if self.isEmpty(qnbr):
            self.front[qnbr] = self.rear[qnbr] = self.free
        else:
            self.next[self.rear[qnbr]] = self.free
            self.rear[qnbr] = self.free
        self.next[self.free] = -1
        self.array[self.free] = item
        self.free = next_free

    def dequeue(self, qnbr):
        if self.isEmpty(qnbr):
            return

        front_index = self.front[qnbr]
        self.front[qnbr] = self.next[front_index]
        self.next[front_index] = self.free
        self.free = front_index
        return self.array[front_index]

    # def delete_right(self, item):
    #     i = self.head
    #
    #     while i is not None:
    #         nxt = i.right
    #         if i.value == item:
    #             if i.left is not None:
    #                 i.left.right = i.right
    #             else:
    #                 self.head = i.right
    #             if i.right:
    #                 i.right.prev = i.prev
    #
    #             else:
    #                 self.rear = i.prev
    #
    #         i = nxt
    #     self.length -= 1
    #     self.print_change()
#
#
# def insert_left(deque, item):
#     curr = Node(item)
#
#     while deque.prev is not None:
#         tmp = deque.prev
#         if not curr:
#             curr = Node(item)
#         curr.right = tmp
#         tmp.left = curr
#     else:
#         deque.end = curr
#
# def delete_right(deque, item):
#     if deque.prev is None:
#         print("queue is empty")
#
#     else:
#         tmp = deque.prev
#         curr.right = tmp
#         tmp.left = curr
#
#
# class Deque:
#     def __init__(self):
