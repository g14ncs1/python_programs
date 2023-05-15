#enter via keyboard 10 positive values , display the biggest of them, their sum, their average 
first = float(input('Enter the 1o number : '))

count = 2
biggest = first
sumNumbers = first

while count < 10:
    temp = float(input('Enter the number %d: ' %count))
    if temp > 0:
        count += 1
        sumNumbers += temp
        if temp > biggest:
            biggest = temp
    else: 
        print("\nError, try again...\n")

average = sumNumbers / 10
print('\nThe sum is:', sumNumbers,'\nThe biggest number is:', biggest,'\nThe average is: ', average)