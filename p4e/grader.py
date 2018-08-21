scoreInput = input('Please enter a score between 0.0 and 1.0.\n')

try:
    score = float(scoreInput)

    if score >= 0.9 and score <= 1:
        print('A')
    elif score >= 0.8 and score < 0.9:
        print('B')
    elif score >= 0.7 and score < 0.8:
        print('C')
    elif score >= 0.6 and score < 0.7:
        print('D')
    elif score < 0.6 and score >= 0:
        print('F')
    else:
        print('Score must be a numberical value between 0.0 and 1.0')
except:
    print('Score must be a numberical value between 0.0 and 1.0')
