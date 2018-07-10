text = open('mbox-short.txt')
d = dict()

for lines in text:
    if not lines.startswith('From '): continue
    words = lines.split()
    addMe = words[2]
    if addMe not in d:
        d[addMe] = 1
    else:
        d[addMe] = d[addMe] + 1


print(d)

for key in d:
        print(key, d[key])
# use me to print!!!
#counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
#for key in counts:
#    print(key, counts[key])
