fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print ('Unable to open', fname)
    exit()
text = fhand.read()

newText = text.upper()

print(newText)
