#enter via keyboard a number, print its multiplication table from 1 to 10 using a for loop
number = float(input('Enter a value to print its multiplication table: '))
for i in range(11):
    multiplication = number * i
    print(number,'x',i,'=',multiplication)
