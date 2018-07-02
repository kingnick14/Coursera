fname = input('Enter a file name: ')
ccount = 0
confTotal = 0
conf = None
confFlat = 0.0
try:
    fhand = open(fname)
except:
    print ('Unable to open', fname)
    exit()

for line in fhand:
    #line = line.rstrip()
    if line.find('X-DSPAM-Confidence:'):
        firstPos = line.find('X-DSPAM-Confidence:')
        print(firstPos)#endPos =
        conf = line[firstPos+1:]
        confFloat = float(conf)
        confTotal = confTotal + confFloat
        ccount = ccount + 1


avgConf = confTotal / ccount
print('Average spam confidence:', avgConf)
