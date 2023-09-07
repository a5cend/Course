s = 'word word2 Python php go C'
stop = ['Python', 'php', 'go', 'C']

filtered = list(filter(lambda x: x not in stop, s.split(' ')))
filtered_string = ' '.join(filtered)
print(filtered_string)
