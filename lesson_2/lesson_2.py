# def arg(a, b, c=2, d=3):
#     return a + b + c + d


# print(arg(1, 2))
# print(arg(1, 2, d=0))
# print(arg(1, 2, 0, 0))

# ------------------------------
# def range_arg(a, b, c, d):
#     return a + ' ' + b + ' ' + c + ' ' + d


# print(range_arg('1', '2', '3', '4'))
# print(range_arg('1', '2', c='5', d='6'))

# ------------------------------
# def quad(side):
#     return side * 4, side ** 2


# print(quad(3))
# p, s = quad(3)
# print(p)
# print(s)


# ------------------------------
# def add(*args):
#     value = 0

    # for item in args:
    #     if isinstance(item, (int, float)):
    #         value += item
    #     else:
    #         print(f'ignore "{item}"')

    # return value


# total = add(1, 'function', 2, 3, 4, 'python', 5.0, 'kwargs')
# print('Total: ', total)


# ------------------------------
def print_kwargs(**kwargs):
    print(kwargs)       # отображает словарь


print_kwargs(kone='One', ktwo=2, kthree=3.0)
