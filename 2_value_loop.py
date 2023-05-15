#enter via 
while True:
    value_1 = float(input('Enter the 1st value: '))
    value_2 = float(input('Enter the 2nd value: '))

    if value_2 > value_1:
        print('\nThe second value is bigger than the first\n')
        break
    else:
        print('\nEnter two values, the 2nd must be bigger than the first\n')
