list_values = []

i = 1 #starts as 0 

while len(list_values) <= 10:
    
    value = float(input('Enter the %do value of the list: ' %i))
    
    if i == 1:
        list_values.append(value)
        i += 1
    elif value > list_values[i-2]: #i - 2 because the check is only made when the 2nd value is added to the list, whose index is 1, 
        list_values.append(value)
        i += 1
    else:
        print('\nInvalid value, try again...\n')

print('The list is: ', list_values)