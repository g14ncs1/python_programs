#enter via keyboard the value of a purchase and the dollar quotation, exibit the type of card and exibit entered info + points
points = [1,1.2,1.5,2.0]
dollar_value = 0

real_value = float(input('Enter the value of the purchase: '))
quotation = float(input('Enter the quotation of the dollar: '))
dollar_value = real_value / quotation

while True:
    card = int(input('\n1 - Brass\n2 - Silver\n3 - Gold\n4 - Diamond\n\nEnter the type of card used: ')) - 1 #card - 1 to match the index of the list

    if 0 <= card < 4:
        break
    else:
        print('\nInvalid value, try again...')

print("\nThe value of the purchase in 'BRL' is: %.2f" %real_value ,"\nThe value of the purchase in 'USD' is: %.2f" %dollar_value ,"\nThe total of points is: ", points[card])