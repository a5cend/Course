def positive_count(list1):
    k = 0
    for i in list1:
        if i > 0:
            k += 1
    return k


print(positive_count([1, -2, 3, -4, -5]))
# 2
