#script that calculates college average
flag = 0 #number of flunks

def stats(average,t1,t2,flag):
    if average > 5:
        print('You have been aproved. Your average was:', average)

    else:
        print('You have been reproved. Your average was:', average)

        if flag == 0:
            t3 = float(input('Enter the result of your 3rd test: '))
            flag = 1

            if t2 > t1:
                average(t2,t3,flag)
            else:
                average(t1,t3,flag)

def average(t1,t2,flag):
    average = (t1 + 2*t2) / 3
    stats(average,t1,t2,flag)

t1 = float(input('Enter the result of your 1st test: '))
t2 = float(input('Enter the result of your 2nd test: '))
