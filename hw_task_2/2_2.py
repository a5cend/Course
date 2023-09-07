lst = [1, 2, 5, 8, 11]
p = 2

f = list(filter(lambda x: x % p == 0, lst))
print(f)
