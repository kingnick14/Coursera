text = open('mbox-short.txt')
d = dict()
for lines in text:
    words = lines.split()
    for word[2] in words:
        d[word] = d.get(word[2],0) + 1
