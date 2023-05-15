#calculate a rectangles area and classify it as big terrain (if area > 100) or small terrain (if area <= 100)
base = float(input('Enter the base of the rectangle: '))
height = float(input('Enter the height of the rectangle: '))
area = base * height

if area > 100:
    print('\nBig terrain')
elif area <= 100:
    print('\nSmall terrain')