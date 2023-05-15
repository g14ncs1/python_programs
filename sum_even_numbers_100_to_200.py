#exibit the sum of the even numbers from 100 to 200 using for loop
sum = 0

for i in range(100, 201, 2): #(starting point, ending point, step)
    sum = sum + i

print("The sum is equal: ", sum)