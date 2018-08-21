inp = input('Enter a file name: ')

text = open(inp)
d = dict()

for lines in text:
    words = lines.split()
    if not lines.startswith('From '): continue
    email = words[1]
    if email not in d:
        d[email] = 1
    else:
        d[email] += 1



##### works but dont know how to store key
##### most = max(d, key=d.get)

most = 0
mostEmail = None

for email in d:
    if most == None or d[email] > most:
        most = d[email]
        mostEmail = email

print(mostEmail, most)
