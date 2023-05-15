#enter via keyboard the aceleration, initial velocity and time, calculate and classify the velocity
a = float(input('Enter the aceleration: '))
v0 = float(input('Enter the initial velocity: '))
t = float(input('Enter the time of the course: '))
v = 3.6*(v0 + a*t)

if v <= 40:
    print('\nVeicle is too slow')
if 40 < v <= 60:
    print('\nAllowed velocity')
if 60 < v <= 80:
    print('\nVelocity of a cruiser')
if 80 < v <= 120:
    print('\nVeicle is fast')
if v > 120:
    print('\nVeicle is too fast')
