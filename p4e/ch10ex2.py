inp = input('Enter a file name: ')

text = open(inp)
d = dict()

for lines in text:
    if not lines.startswith('From '): continue
    words = lines.split()
    time = words[5]
    numbs = time.split(':')
    hour = numbs[0]
    if not hour in d:
        d[hour] = 1
    else:
        d[hour] += 1


lst = []

for key, val in list(d.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
