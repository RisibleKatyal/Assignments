#Question 1

grade= float(input("Please enter your marks "))

if grade<25:
    print("Your final grade is F")
elif grade>=25 and grade<45:
    print("Your final grade is E")
elif grade>=45 and grade<50:
    print("Your final grade is D")
elif grade>=50 and grade<60:
    print("Your final grade is C")
elif grade>=60 and grade<80:
    print("Your final grade is B")
elif grade>=80 and grade<=100:
    print("Your final grade is A")
else:
    print("Error: You cannot have the entered number of marks!")
    
    
#Question 2

year= int(input("Please enter year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("The year ",year," is a leap year!")
    else:
        print("The year ",year," is not a leap year :(")
elif year % 4 == 0:
    print("The year ",year," is a leap year!")
else:
    print("The year ",year," is not a leap year :(")


#Question 3

from random import randint

for loop_variable in range(10):
    no1 = randint(0,10)
    no2 = randint(0,10)
    if int(input('Question: ' + str(no1) + ' x ' + str(no2) + ' = ')) == no1 * no2: print('Right!')
    else: print('Wrong. The answer is ', no1 * no2)


#Question 4

number=1
while number<200:
    if number%5 == 2 and number%6 == 3 and number%7 == 2:
        print("The number is: " + str(number))
    number = number + 1
