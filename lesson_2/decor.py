def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'{result} руб.'
    return wrapper


def price_calculation1(price, tax):
    return price * (tax + 1)


@currency
def price_calculation2(price, tax):
    return price * (tax + 1)


price_calculation_decorator = currency(price_calculation1)
print(price_calculation1(100, 0.2))
print(price_calculation_decorator(100, 0.2))

print(price_calculation2(100, 0.2))
