elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

sort = [0] * len(elements)

for i in range(len(elements)):
    numbers = list(map(lambda x: x[1], elements))
    index_min = numbers.index(min(numbers))
    sort[i] = elements[index_min]
    elements.remove(elements[index_min])

print(sort)
