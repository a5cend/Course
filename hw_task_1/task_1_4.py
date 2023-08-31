def condition(chislo):
    if chislo > 100 or chislo < -100:
        return '-'
    else:
        return '+'


print(condition(-200))
# -

print(condition(20))
# +
