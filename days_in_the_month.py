#enter via keyboard the number of a month, display its month and the number of days

months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
days = [31,29,31,30,31,30,31,31,30,31,30,31]

while True:
    wanted_month = int(input('Enter the wanted months number: ')) - 1 #i = index - 1 (so it matches the lists index)

    if 0 < wanted_month < 12:
        break
    else:
        print('\nInvalid month, try again...\n')

months_name = months[wanted_month]
days_of_month = days[wanted_month]

print('\n',months_name,'has',days_of_month,'days')