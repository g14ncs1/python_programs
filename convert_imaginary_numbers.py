#enter a imaginary number in the rectangular form, exibit it in the polar form
import math

def rectangular_polar(real_number, imaginary_number):
    real_number
    imaginary_number

    #for r + ji
    if real_number > 0 and imaginary_number > 0:
        print('\nRectangular: ', real_number, ' + j', imaginary_number)
        
        module = round(math.sqrt(math.pow(real_number, 2)) + (math.pow(imaginary_number, 2)), 2)

        angle_radius = math.atan(abs(imaginary_number) / abs(real_number))
        angle_degrees = round((math.degrees(angle_radius)), 2)

    #for r - ji
    if real_number > 0 and imaginary_number < 0:
        print('\nRectangular: ', real_number, ' - j', imaginary_number)
        
        module = round(math.sqrt(math.pow(real_number, 2)) + (math.pow(imaginary_number, 2)), 2)

        angle_radius = math.atan(abs(imaginary.number) / abs(real_number))
        angle_degrees = round((math.degrees(angle_radius)) * (-1), 2)

    #for -r + ji
    if real_number < 0 and imaginary_number > 0:
        print('\nRectangular: ', real_number, ' + j', imaginary_number)
        
        module = round(math.sqrt(math.pow(real_number, 2)) + (math.pow(imaginary_number, 2)), 2)

        angle_radius = math.atan(abs(imaginary_number) / abs(real_number))
        angle_degrees = round((180 - math.degrees(angle_radius)), 2)

    #for -r - ji
    if real_number < 0 and imaginary_number < 0:
        print('\nRectangular: ', real_number, ' + j', imaginary_number)
        
        module = round(math.sqrt(math.pow(real_number, 2)) + (math.pow(imaginary_number, 2)), 2)

        angle_radius = math.atan(abs(imaginary_number) / abs(real_number))
        angle_degrees = round((180 - math.degrees(angle_radius)) * (-1), 2)

    print('\nPolar: ', module, ' |', angle_degrees, 'o\n',sep = '')

real = float(input('\nEnter the real number: '))
imaginary = float(input('Enter the imaginary number: '))

rectangular_polar(real, imaginary)