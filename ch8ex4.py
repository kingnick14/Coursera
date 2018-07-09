text = open('romeo.txt')
wordList = []
ddList = []
for line in text:
    line = line.rstrip()
    words = line.split()
    for i in range(len(words)):
        if words[i] in wordList: continue
        wordList.append(words[i])

wordList.sort()

#for i in range(len(wordList)):
#    if i > 0 and wordList[i] == wordList[i-1]:
#        del wordList[i]
#    else:
#        continue
#print(ddList)

print(wordList)

    #list.append(NEW WORD)
