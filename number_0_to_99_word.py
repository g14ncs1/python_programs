#enter via keyboard a number from 0 to 99, output it in full
unit = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
dozen = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
first_dozen = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixsteen','seventeen','eighteen','nineteen']

while True:
    number = int(input('Enter a number from 0 to 99: '))

    if 0 <= number <= 99:
        number_dozen = number // 10
        number_unit = number % 10

        if number >= 20:
            print('\nThe entered number in full is: %s' %dozen[number_dozen])

            if number_unit != 0:
                print('\nThe entered number in full is: %s %s' %(dozen[number_dozen], unit[number_unit]))
                break

            else:
                print('\nThe entered number in full is: %s' %dozen[number_dozen])
                break
        
        elif number >= 10:
            print('\nThe entered number in full is: %s\n' %first_dozen[number_unit])
            break

        else:
            print('\nThe entered number in full is: %s\n' %unit[number_unit])
            break

    else:
        print('\nInvalid input, try again...\n')