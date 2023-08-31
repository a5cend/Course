lst = [2, 4, 5, 8, 9, 13]
for number in range(len(lst)):
    lst[number] *= number
print(lst)
# [0, 4, 10, 24, 36, 65]


lst = [2, 4, 5, 8, 9, 13]
c = 0
while c != len(lst):
    lst[c] *= c
    c += 1
print(lst)
# [0, 4, 10, 24, 36, 65]
