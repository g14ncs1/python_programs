#enter via keyboard how many students are in your class, enter their grades, display the average
students = int(input('How many students are in your class: '))
grades = []

for x in range(students):
    grade = float(input('What is the %do students grade: ' %x))
    grades.append(grade)

average = sum(grades)/students
print('The average grade of your class is: ', average)