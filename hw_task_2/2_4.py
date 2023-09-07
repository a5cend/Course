l1 = [1, 2, 'word', 'hello']
l2 = [1, 2, 5, 8, 11]


print(list(filter(lambda x: x in l2, l1)))
