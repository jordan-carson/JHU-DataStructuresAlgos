#
#
# def run_prefix(expr):
#     size = len(expr)
#
#     rev_stack = Stack()
#     op_stack = Stack()
#     conv, store, res = "", "", ""
#
#     op_check = 0
#     if len(expr) == 0:
#         raise Exception('Expression should not be empty.')
#
#     for i in range(len(expr)):
#         if is_operator(i):
#             op_check += 1
#             store += " " + expr[i] + " "
#         else:
#             store += " " + expr[i] + " "
#
#     # if op_check <= 0:
#     #     raise Exception('syntax error')
#
#     print(op_stack.pop(), rev_stack.pop())
#
#     while not rev_stack.is_empty():
#         store = rev_stack.pop()
#
#         if is_operator(store) is True:
#             op_check += 1
#             if op_stack.is_empty():
#                 raise Exception('Empty stack')
#             else:
#                 op1 = op_stack.peek()
#                 op_stack.pop()
#                 op2 = op_stack.peek()
#                 op_stack.pop()
#
#                 res = op1 + op2 + store
#
#                 op_stack.push(res)
#         else:
#             op_stack.push(store)
#
#         while not op_stack.is_empty():
#             conv += op_stack.pop()
#         return conv
#
#     #
#     # valid = True
#     #
#     #
#     #
#     #
#     # for i in range(len(prefix), -1):
#     #     tmp = prefix[i]
#     #     if is_operator(tmp):
#     #         if stack.size > 1:
#     #             op1 = stack.pop()
#     #             op2 = stack.pop()
#     #
#     #             aux = op1 + op2 + prefix[i]
#     #             stack.push(aux)
#     #         else:
#     #             valid = False
#     #     elif is_operands(tmp):
#     #         stack.push(tmp)
#     #
#     #     else:
#     #         valid = False
#     #
#     # if not valid:
#     #     print(prefix)
#     #     print(stack.pop())
#     # else:
#     #     print(prefix)
#
#
