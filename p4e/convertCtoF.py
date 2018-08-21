Cinput = input('Please tell me what the temperature is outside in Celcius\n')

try:
    C = float(Cinput)

    F = (C * (9/5)) + 32

    print('The temperature outside is currently',F,'degrees Fahrenheit!')
except:
    print('Please enter a number, duh!')
