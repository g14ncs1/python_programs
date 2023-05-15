#enter via keyboard a 10 value list, display specified information
list_values = []
i = 1

while i <= 10:
    value = float(input('Enter the %do value of the list: ' %i))
    list_values.append(value)
    i += 1

print('\nThe list is: ', list_values)
print('\nThe smallest value of the list is: ', min(list_values))
print('\nThe biggest value of the list is: ', max(list_values))
print('\nThe sum of the list values is: ', sum(list_values))
print('\nThe average of the lists values is: ', sum(list_values)/10)