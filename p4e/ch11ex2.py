import re
inp = input('Enter a file name: ')
hand = open(inp)
lst = []

for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision:.([0-9]+)', line)
    if len(x) > 0 : lst = lst + x


#lst = [float(num) for num in lst]
### not sure why the above works (found online) but the below doesn't.

for num in lst:
    lst[num] = float(num)

average = sum(lst) / len(lst)

print(average)
