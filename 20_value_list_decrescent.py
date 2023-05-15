#add via keyboard 20 values to a list and exibit them in decrescent order
list_values = []
i = 1

while i <= 20:
    value = float(input('Enter the %do value to the list: ' %i))
    list_values.append(value)
    i += 1

print('\nThe given list is: ', list_values)

list_values.sort(reverse = True) #arranges values in decrescent order

print('\nThe sorted list is: ', list_values)