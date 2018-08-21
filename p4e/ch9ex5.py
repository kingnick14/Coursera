print('python schoolcount.py')
inp = input('Enter a filename: ')
text = open(inp)
d = dict()

for lines in text:
    words = lines.split()
    if not lines.startswith ("From "): continue
    email = words[1]
    firstP = email.find('@')
    domain= email[firstP+1:]

    if domain not in d:
        d[domain] = 1
    else: d[domain] += 1

print(d)
