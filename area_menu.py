#enter via keyboard the area to be calculated according to the menu
import math #library containing math functions to calculate the areas
import time #library containing function for delay
state = True

while True:
    option = int(input('\n----------------------\n1 - Rectangle\n2 - Square\n3 - Triangle\n4 - Circle\n5 - Exit\n----------------------\n\nEnter the object to calculate its area: '))

    if option == 1:
        base = float(input('\nEnter the objects base: '))
        height = float(input('Enter the objects height: '))
        area = base * height
    elif option == 2:
        edge = float(input('\nEnter the objects edge: '))
        area = edge**2
    elif option == 3:
        base = float(input('\nEnter the objects base: '))
        height = float(input('Enter the objects height: '))
        area = (base * height)/2
    elif option == 4:
        radius = float(input('\nEnter the objects radius: '))
        area = math.pi*radius**2 #math.pi = pi
    elif option == 5:
        print('\nExiting program...')
        time.sleep(1)
        break
    else:
        print('\nInvalid value, try again...')
        state = False

    if state == True:
        print('\nThe calculated area is: ', area)