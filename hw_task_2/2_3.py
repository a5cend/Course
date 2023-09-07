def func1(*args):
    t = list()
    for item in args:
        if isinstance(item, str):
            t.append(item)
    return tuple(t)


def func2(*args):
    return tuple(filter(lambda x: isinstance(x, str), args))


print(func1(1, 2, 'word', 'hello', True))
print(func2(1, 2, 'word', 'hello', True))
