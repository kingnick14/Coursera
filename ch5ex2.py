total = 0
average = None
count = 0
min = None
max = None

while True:
    inputno = input('Enter a number:')
    try:
        if inputno == 'done':
            break
        else:
            number = float(inputno)
            total = total + number
            count = count + 1
            if min is None or min > number:
                min = number
            elif max is None or max < number:
                max = number
    except:
        print('invalid input!')
        continue

total = int(total)
average = total / count
print('total:', total, 'count:', count, 'average:', average, 'max:', max,'min:', min)
