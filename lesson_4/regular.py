import re

print(re.match(r'\d{2}', 'string, 123 - no string'))
print(re.match(r'\d{2}', '123 - no string'))
print(re.match(r'\d{2}', '123 - no string').group())
print(re.match(r'\d{2}', 'string'))

print(re.search(r'\d{2}', 'string, 123 - no string'))
print(re.search(r'\d{2}', 'string, 123 - no string').group())

print(re.findall(r'\d{2}', '12 - no string, 34 - blablabla, 56'))

print(re.fullmatch(r'\d{3}', '123 - no string'))
print(re.fullmatch(r'\d{3}', '123').group())


def regexp(s):
    if re.fullmatch(r'\w{5,15}@\w{2,6}\.\w{2,3}', s):
        return True
    else:
        return False


print(regexp('solovev@mail.ru'))
print(regexp('solovyov@yandex.net'))
print(regexp('solovyov!@mail.com'))
