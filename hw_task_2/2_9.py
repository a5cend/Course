from functools import reduce
import time


def decor(fn):
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        fn(*args, **kwargs)
        return f'Затраченное время: {time.perf_counter() - t0} секунд'
    return wrapper


@decor
def func1():
    print('func1 is on')
    calc_sum = reduce(lambda x, y: x + y, range(1, int(10e5)))
    return calc_sum


@decor
def func2():
    print('func2 is on')
    calc_sum = reduce(lambda x, y: x + y, range(1, int(10e6)))
    return calc_sum


print(func1())
print(func2())
