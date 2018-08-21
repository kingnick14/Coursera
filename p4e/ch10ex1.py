inp = input('Enter a file name: ')

text = open(inp)
d = dict()

for lines in text:
    if not lines.startswith('From '): continue
    words = lines.split()
    email = words[1]
    if not email in d:
        d[email] = 1
    else:
        d[email] += 1

lst = list()
for key,val in list(d.items()):
    lst.append((val,key))

lst.sort(reverse=True)

for key, val in lst[0:1]:
    print(val,key)
