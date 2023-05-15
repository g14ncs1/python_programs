#enter 3 values, calculate its average
def average(value_1,value_2,value_3):
    average = (value_1 + value_2 + value_3) /3
    return average

    value_1 = float(input('\nEnter the first value: '))
    value_2 = float(input('Enter the second value: '))
    value_3 = float(input('Enter the third value: '))
    
    average = average(value_1,value_2,value_3)
    print('\nThe average of the given values is: ', round(average,2))