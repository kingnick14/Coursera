text = open("romeo.txt")
wordDict = dict()
i = 0

for line in text:
    words = line.split()
    for word in words:
        wordDict[word] = i
        i = i + 1

print (wordDict)
while True:
    inp = input ('see if a word appears in the text:')
    if inp == 'done' : break
    elif inp in wordDict:
        print ("'",inp, "' appears in the text!")
    else:
        print("'",inp, "' does NOT appear in the text!")
