import os
from argparse import ArgumentParser
from typing import Union, AnyStr, SupportsIndex, SupportsInt
import json

# module imports
from util import LinkedStack as Stack, is_operands, is_operator, PATH, LinkedList, create_list


def read_input(file_name: Union[AnyStr]):
    """
    Reads input file - returns the results as a list.
    Args:
        file_name:

    Returns:

    """
    path = os.path.join(PATH, file_name)
    return open(path, 'r').read().split('\n')


def convert_to_list(input) -> list:
    return [str(i) for i in input]


def prefix_to_postfix(prefix: LinkedList):
    is_valid: bool = True
    operator = prefix.remove(0)
    op1 = LinkedList()
    op2 = LinkedList()

    output = LinkedList()
    msg = None

    if is_valid and prefix.size != 0:
        if is_operator(prefix.head.data[0]):
            op1 = prefix_to_postfix(prefix)

        elif is_operands(prefix.head.data[0]):
            op1.insert_index(prefix.remove(0), 0)

        else:
            is_valid = False
            msg = f"Error: Invalid Characters {prefix.head.data[0]}"

    if is_valid and prefix.size != 0:
        if is_operator(prefix.head.data[0]):
            op2 = prefix_to_postfix(prefix)

        elif is_operands(prefix.head.data[0]):
            op2.insert_index(prefix.remove(0), 0)

        else:
            is_valid = False
            msg = f"Error: Invalid Characters {prefix.head.data[0]}"

    if is_valid:
        while not op1.is_empty():
            output.insert_index(op1.remove(0), output.size)

        while not op2.is_empty():
            output.insert_index(op2.remove(0), output.size)

        output.insert_index(operator, output.size)

    if msg:
        print(msg)  # error msg for understanding issues..

    return output


def stack_pre_to_post(expr: Union[AnyStr]) -> AnyStr:
    """
    Function to Convert Prefix to Postfix.

    Examples:
        >>> expr = "*AB"
        >>> postfix = stack_pre_to_post(expr)

    Args:
        expr (str): prefix string

    Returns:
        converted postfix string
    """

    postfix = Stack()

    is_valid = True
    i = len(expr) - 1
    while i >= 0:
        if is_operator(expr[i]):
            if postfix.size() > 1:
                op1 = postfix.pop()
                op2 = postfix.pop()
                res = op1 + op2 + expr[i]
                postfix.push(res)
            else:
                is_valid = False

        elif is_operands(expr[i]):
            postfix.push(expr[i])
        else:
            is_valid = False
        i -= 1

    return "Exception: Invalid Prefix Expression" if is_valid is False else postfix.pop()


def writer(pointer, index: Union[None, SupportsIndex, SupportsInt], expr, res, readable=False):
    if readable:
        if index == 0:
            pointer("*******Lab 1 Results*******\n")
        pointer(f"Index:{index} Input:{expr} Result:{res}\n")
    else:
        pointer(json.dumps(dict(Prefix=expr, Postfix=res)))


def main():
    parser = ArgumentParser(description="Prefix to Postfix Converter")
    parser.add_argument("--func", default="stack", help="stack or linked-list", required=True)
    parser.add_argument("--input_file", default="input.txt", help="File containing prefix data for Lab 1",
                        required=False)
    parser.add_argument("--output_name", default="output", help="output filename", required=False)
    parser.add_argument(
        "--out", choices=['json', 'txt', 'print'], default='print', help="choose output type", required=False
    )

    args = parser.parse_args()
    inp = read_input(args.input_file)

    print_res: bool = True if args.out == "print" else False
    out_type: str = args.out if print_res is False else ""
    out_file = open(args.output_name + "." + out_type, "w") if not print_res else None

    result = dict()

    # made a dic to determine which function to used based on args.func
    dico = {
        'stack': stack_pre_to_post,
        'recursion': prefix_to_postfix,
    }
    for idx, expr in enumerate(inp):
        # we need to create before applying the prefix_to_postfix function
        expr = create_list(expr) if args.func in ['recursion'] else expr
        res = dico[args.func](expr)
        result[expr] = res
        if print_res is True:
            writer(print, idx, expr, res)
        if out_type == "txt":
            writer(out_file.write, idx, expr, res)
        if out_type == "json":
            json.dump(result, out_file)

    return True


if __name__ == '__main__':
    main()
