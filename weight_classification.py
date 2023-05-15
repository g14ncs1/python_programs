#enter via keyboard weight and height, calculate and classify it 
weight = float(input('Enter the weight: '))
height = float(input('Enter the height: '))
relation = weight / pow(height,2)

if relation < 20:
    print('\nBellow the ideal weight')
if 20 <= relation < 25:
    print('\nIdeal weight')
if relation >= 25:
    print('\nAbove the ideal weight')