fhand = open('mbox-short2.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 and words[0] != 'From' and len(words) = 2 : continue

    print(words[2])
