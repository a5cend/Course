import pandas as pd


def check(list1, list2):
    arr = pd.Series(list1)
    print(arr[list2])


def check2(list1, list2):
    if len(list1) == len(list2):
        return pd.Series(list1, index=list2)


print(check2([3, 5, 7], [3, 1, 2]))
