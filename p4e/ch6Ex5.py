str = 'X-DSPAM-Confidence:0.8475'

colon = str.find(':')

print(colon)

conf = str[colon+1:]

confFloat = float(conf)

print(confFloat)
print(type(confFloat))
