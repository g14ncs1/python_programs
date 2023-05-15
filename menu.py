#select 1 of 5 options in the menu
def menu(menu_list):
    count = 1
    
    for i in menu_list:
        print(count,'-',i)
        count += 1

    while True:
        query = int(input('\nEnter the wanted option: '))

        if 0 < query < count:
            break
        
        else:
            print('\nInvalid option, try again...\n')
    
    return(query)

i = menu(['Open','Close','Exclude','Save','Exit'])
print('\nThe wanted option was:', i)