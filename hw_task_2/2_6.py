def decor(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if type(result) != int:
            raise Exception(f'"{result}" is not int')
        else:
            return f'"{result}" is int'
    return wrapper


@decor
def func1():
    return 2


@decor
def func2():
    return 'word'


print(func1())
print(func2())
