def computegrade(score1):
    if score1 >= 0.9 and score1 <= 1:
        print('A')
    elif score1 >= 0.8 and score1 < 0.9:
        print('B')
    elif score1 >= 0.7 and score1 < 0.8:
        print('C')
    elif score1 >= 0.6 and score1 < 0.7:
        print('D')
    elif score1 < 0.6 and score1 >= 0:
        print('F')
    else:
        print('Score must be a numerical value between 0.0 and 1.0')

scoreInput = input('Please enter a score between 0.0 and 1.0.\n')

try:
    score = float(scoreInput)
    computegrade(score)
except:
    print('Score must be a numerical value between 0.0 and 1.0')
