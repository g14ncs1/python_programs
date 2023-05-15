#exibit the multiplication table to 20 with a 10 interval between them, solicit the user enter a key to proceed
for x in range(1, 21, 1):
    key = input("Enter 'Y' to proceed: ")

    if key == 'y' or key == 'Y':
        for i in range(11):
            multiplication = x * i
            print(x,'x',i,'=',multiplication)