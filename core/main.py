import os
from argparse import ArgumentParser
# module imports
from core.util import LinkedStack as Stack, is_operands, is_operator, PATH, InvalidPrefixException, StackSyntaxException

# import typer
# util = typer.Typer()


def read_input(file_name):
    path = os.path.join(PATH, file_name)
    return open(path, 'r').read().split('\n')


def converter(expr):
    postfix = Stack()

    is_valid = True
    i = len(expr) - 1
    while i >= 0:
        #  Check whether given prefix location
        #  at [i] is an operator or not
        if is_operator(expr[i]):
            #  When operator exist
            #  Check that two operands exist or not
            if postfix.size() > 1:
                op1 = postfix.pop()
                op2 = postfix.pop()
                res = op1 + op2 + expr[i]
                postfix.push(res)
            else:
                is_valid = False

        elif is_operands(expr[i]):
            #  When get valid operands
            postfix.push(expr[i])
        else :
            #  Invalid operands or operator
            is_valid = False

        i -= 1

    return "Exception: Invalid Prefix Expression" if is_valid is False else postfix.pop()
    # if is_valid is False:
    #     print(f"Invalid Prefix Expression: {expr}")
    # else:
    #     print(dict(Prefix=expr, Postfix=postfix.pop()))


def main():
    parser = ArgumentParser(description="Prefix to Postfix Converter")
    parser.add_argument("--filename", default="input.txt", help="File containing prefix data for Lab 1")

    args = parser.parse_args()
    inp = read_input(args.filename)
    result = dict()
    for i in inp:
        res = converter(i)
        result[i] = res

    return result


if __name__ == '__main__':
    print(main())