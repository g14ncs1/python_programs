#calculate the sum  of the sequence, appending a value entered via keyboard
list_values = [2,5,10,17,26]
sum = 0
while True:
    value = int(input('Enter a value between 0 and 100: '))

    if 0 < value < 100:
        list_values.append(value)
        
        for x in range(len(list_values)):
            sum = sum + list_values[x]

        print('The sum of the lists values is: ', sum)
        break
    
    else:
        print('\nInvalid input, try again...\n')