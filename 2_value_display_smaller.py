#enter via keyboard 2 distinct values, exibit the smaller one
value_1 = input('Enter the 1st value: ')
value_2 = input('Enter the 2nd value: ')

while True:
    if value_1 == value_2:
        print('\nThe two values are equal, try again...\n')
        value_1 = input('Enter the 1st value: ')
        value_2 = input('Enter the 2nd value: ')
    elif value_1 < value_2:
        print('\nThe smaller value is', value_1)
        break
    elif value_2 < value_1:
        print('\nThe smaller value is', value_2)
        break