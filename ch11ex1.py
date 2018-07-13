import re
hand = open('mbox.txt')
count = 0

# would be nice to add this to a while loop so that it can be run multiple timesself.
# did not succeed, after first iteration, count keeps same value as first loop
inp = input('Enter a regular expression: ')

for line in hand:
    line = line.rstrip()
    if re.findall(inp, line):
        count += 1
print('mbox.txt had',count,'lines that matched',inp)
