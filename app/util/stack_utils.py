from app.util.constants import EMPTY_STR


class Node:
    def __init__(self, data, head):
        self.data = data
        self.next = head


class Stack:
    def __init__(self):
        self.items = list()

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.items

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, item):
        return self.items[item]

    @property
    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == list() or len(self.items) == 0

    def push(self, new_item: str):
        self.items.append(new_item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size - 1]

    def to_list(self):
        return self.items


class StackList:
    def __init__(self):
        self.items = list()

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        yield from self.items

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, item):
        return self.items[item]


class LinkedStack:
    def __init__(self) :
        self.head = None
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        if self.size() > 0:
            return False
        return True

    def peek(self):
        if not self.is_empty():
            return self.head.data
        return EMPTY_STR

    def push(self, data):
        self.head = Node(data, self.head)
        self.count += 1

    def pop(self):
        temp = EMPTY_STR
        if self.is_empty() is False:
            temp = self.head.data
            self.head = self.head.next
            self.count -= 1
        return temp


def is_operands(text):
    if ('0' <= text <= '9') or ('a' <= text <= 'z') or ('A' <= text <= 'Z'):
        return True
    return False
