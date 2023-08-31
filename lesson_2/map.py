def square(number):
    return number ** 2


# lst = [1, 2, 3, 4]
# print(list(map(square, lst)))

# lst = ['1', '2', '3', '4']
# print(list(map(int, lst)))
# print(list(map(float, lst)))

# lst = 'abcde'
# print(list(map(lambda x: x.upper(), lst)))
# print(list(lst.upper()))

# print(''.join(list(map(lambda x: x.upper(), lst))))
# print(''.join(list(lst.upper())))

lst = ['one', 'two', 'three']
print(list(map(lambda x: len(x), lst)))
print(list(map(len, lst)))
