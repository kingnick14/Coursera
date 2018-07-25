total = 0
average = None
count = 0

while True:
    inputno = input('Enter a number:')
    try:
        if inputno == 'done':
            break
        else:
            number = float(inputno)
            total = total + number
            count = count + 1

    except:
        print('invalid input!')
        continue

total = int(total)
average = total / count
print(total, count, average)
