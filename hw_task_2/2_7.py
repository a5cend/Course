def decor(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        try:
            if type(result) != int:
                raise Exception(f'"{result}" is not int')
            else:
                return f'"{result}" is int'
        except Exception:
            return fn(*args, **kwargs)
    return wrapper


@decor
def func1():
    print('func1 is on')
    return 2


@decor
def func2():
    print('func2 is on')
    return 'word'


print(func1())
print(func2())
