#simulation of manipulation of files menu
import time

while True:
    input("Click 'enter' to access the menu\n\n--------------------------------\n\n")
    option = int(input('\n1 - Open\n2 - Save\n3 - Delete\n4 - Export\n5 - Exit\n\n--------------------------------\n\nEnter one of the above options: '))

    if option == 1:
        print('\nOpening file...')
        time.sleep(3)
        break
    elif option == 2:
        print('Saving file...')
        time.sleep(3)
        break
    elif option == 3:
        print('Deleting file...')
        time.sleep(3)
        break
    elif option == 4:
        print('Exporting file...')
        time.sleep(3)
        break   
    elif option == 5:
        print('Exiting program...')
        time.sleep(3)
        break
    else:
        print('Invalid value, try again...')