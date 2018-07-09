text = open('mbox-short.txt')
count = 0
for line in text:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[1])
    count = count + 1

print('there were', count, 'lines int he file with From as the first word')
