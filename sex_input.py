#enter via keyboard the sex of the user, accept only 'F' or 'M' as valid answers
while True:

    sex = input('Enter your sex: ')

    if sex == 'f' or sex == 'F':
        print('\nYou are a female')
        break
    elif sex == 'm' or sex == 'M':
        print('\nYou are a male')
        break
    else:
        print('\nInvalid value, try again...\n')