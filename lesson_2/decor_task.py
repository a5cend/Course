def decorator(func):
    def wrapper(*args, **kwargs):
        print('Расчет...')
        result = func(*args, **kwargs)
        print(f'Результат вычислений: {result}')
        return result
    return wrapper


@decorator
def f1(number):
    return number ** 2


@decorator
def f2(number):
    return number * 2


f1(3)
f2(3)
