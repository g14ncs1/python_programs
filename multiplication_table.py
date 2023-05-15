#enter via keyboard natural number except 0, exibit the number's multiplication table from 1 to 10
while True:
    number = float(input('Enter a natural number: '))
    i = 1

    if number > 0:
        while i <= 10:
            print(number,'x',i,'=',number*i)
            i += 1
        break
    
    else:
        print('\nInvalid value, try again...\n')
