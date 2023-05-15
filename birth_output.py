#enter via keyboard a date of birth, output the date plus the month word
month_word = ('January','Febuary','March','April','May','June','July','August','September','October','November','December')

while True:
    date = input('Enter with your date of birth in the format (dd/mm/yyyy): ')
    print('Input: ', date)

    date_separated = date.split('/')

    day = int(date_separated[0])
    month = int(date_separated[1])
    year = int(date_separated[2])

    if 0 < day <= 31 and 0 < month <= 12:
        print('Output: ', day, month_word[month-1], 'of', year, '\n')
        break
    else:
        print('\nInvalid value, try again...\n')
    