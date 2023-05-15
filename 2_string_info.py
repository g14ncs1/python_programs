#enter via keyboard 2 strings, display it's similarities
string_1 = input('Enter the 1st string: ')
string_2 = input('Enter the 2nd string: ')

print('\nThe string "%s" has %d characters' %(string_1, len(string_1)))
print('\nThe string "%s" has %d characters' %(string_2, len(string_2)))

if len(string_1) != len(string_2):
    print('The two strings have diferent sizes')
    print('The two strings have the same and content')
else:
    print('The two strings have the same size')

    if string_1 == string_2:
        print('The two strings have the same value')
    else:
        print('The two strings have different values')