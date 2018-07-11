import string
inp = input('Enter a file name: ')

text = open(inp)
d = dict()

for lines in text:
    lines = lines.translate(lines.maketrans(' ',' ',string.punctuation))
    lines = lines.translate(lines.maketrans(' ',' ',string.digits))
    lines = lines.translate(lines.maketrans(' ',' ',string.whitespace))
    lines = lines.lower()
    for letter in lines:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

lst = []

for key, val in list(d.items()):
    lst.append((val,key))

lst.sort(reverse=True)

for val, key in lst:
    print(key, val)
