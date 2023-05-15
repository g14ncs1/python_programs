#enter via keyboard a 10 value list, enter a multiplicative constant that multiplies each value and stores the answer in their respective positions
list_values = []
i = 1

while i <= 10:
    value = float(input('Enter the %do value: ' %i))
    
    if type(value) == float or type(value) == int:
        list_values.append(value) #adds new value to the list
        i += 1
    else:
        print('\nInvalid value, try again...\n')

print('\nThis is the list you have entered: ', list_values)
constant = float(input('\nEnter the multiplicative constant: '))
i = 1 #resets the index to keep from declaring more variables

while i < 10:
    list_values[i-1] = constant * list_values[i-1] #changes the original values by the multiplicated by the constant
    i += 1

print('\nThe list multiplicated by the given constant is: ', list_values)