from .stack_utils import *
from .constants import *
from .exceptions import *
from .data_structures import *


def create_list(input):
    ll = LinkedList()
    for i in input:
        ll.insert(i)
    return ll