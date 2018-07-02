def counter(inputWord,inputLetter):
    word = str(inputWord)
    letter = str(inputLetter)
    count = 0
    for checker in word:
        if checker == letter:
            count = count + 1
    return count

inputWord = input('Please let me know what word you would like to analyze:\n')
inputLetter = input('And now what letter or digit would you like to count?\n')

finalCount = counter(inputWord,inputLetter)

print(finalCount)
