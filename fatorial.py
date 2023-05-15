#enter via keyboard a natural number, output its fatorial, ask to continue
decision = True

while decision == True:
    number = int(input('\nEnter a positive number: '))

    if number >= 0:
        result = 1

        for i in range(number, 1, -1):
            result *= i
            
            if i == number:
                expression = str(i)
            else:
                expression = str(expression) + " x " + str(i)
    
    else:
        print('\nInvalid number...\n')

    print(expression,'=',result)

    while True:
        retry = input('\nDo you want to try again? Yes(y) or No(n)? ')
        
        if retry == 'y' or retry == 'Y':
            decision = True
            break
        elif retry == 'n' or retry == 'N':
            decision = False
            break