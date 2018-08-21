
def computePay(hours,rate):
    if hours > 40.0:
        overtimePay = (rate * 40.0) + (rate * 1.5)*(hours-40.0)
        print('Due to overtime policy, the employee salary is', overtimePay,' dollars.')
    else:
        normalPay = rate * hours
        print('Having worked', hours,'hours, the employee pay is', normalPay,' dollars.')

inputHours = input('Please enter the hours!\n')

try:
    hours1 = float(inputHours)
    inputRate = input('Please enter the employees rate\n')
    rate1 = float(inputRate)

    computePay(hours1,rate1)

except:
    print('Next time, please enter only numbers to calculate pay')
