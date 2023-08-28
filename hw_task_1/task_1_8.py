def exc(s):
    if type(s) is not str:
        raise Exception('This is not a string!')
    new_s = ''
    for i in s.split(' '):
        new_s += i[0]
    return new_s



print(exc('Hello World!'))
