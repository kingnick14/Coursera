fname = input('Enter a file name: ')
ccount = 0
confTotal = 0
conf = None
confFlat = 0.0
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print ("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    print ('Unable to open', fname)
    exit()

for line in fhand:
    if not line.find('X-DSPAM-Confidence:') == -1:
        firstPos = line.find(':')
        conf = line[firstPos+1:]
        confFloat = float(conf)
        confTotal = confTotal + confFloat
        ccount = ccount + 1


avgConf = confTotal / ccount

writtenFile = open('aaaaaaaaaaaaaaa.txt','w')
print('Average spam confidence :' + str(avgConf))
lineWriter = 'Average spam confidence: ' + str(avgConf)
writtenFile.write(lineWriter)
writtenFile.close()
