storedNum = []

while (True):
    inp = input('Enter a number: ')

    try:
        if inp == 'done': break
        number = float(inp)
        storedNum.append(number)
    except:
        print('DAS GEHT GAR NICHT! ENTER A NUMBER PLEASE!')

if len(storedNum) < 1:
    print ('No numbers entered.')
else:
    maxNum = max(storedNum)
    minNum = min(storedNum)

    print ('Maximum:',maxNum,'\nMinimum:',minNum)
