#Chinmay Goyal
#Mechanical_21107101
#Python Assignment 5


#Question 1

in1=input("Enter string here: ")
#Creating empty string
rev=""

#Each element from inputstring is added from left side 
for i in in1:
    rev=i+rev

print(rev)        

#Question 2
lowlmt=int(input("Insert lower limit for range: "))
uplmt=int(input("Insert upper limit for range: "))

givennum=int(input("Insert chosen number for checking multiples: "))

for i in range (lowlmt,uplmt):
    if i%givennum==0:
        print(i)
    else:
        continue
    
print("No more multiples")   



#Question 3

#First we check if the sides of the triangle make a triangle

A1 = int(input("Enter length 1: "))
A2 = int(input("Enter length 2: "))
A3 = int(input("Enter length 3: "))

a = A1 + A2
b = A2 + A3
c = A1 + A3


#If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle.
#Checking for this condition
check_1 = a > A3
check_2 = b > A1
check_3 = c > A2

#Checking if the three conditions are true or false

triangle_check = str(check_1 & check_2 & check_3)

#Use Heron's formula if the sides form a triangle
s = round((A1 + A2 + A3) / 2)
ar_square = s * (s - A1) * (s - A2) * (s - A3)


if triangle_check == "True":
    area = (ar_square) ** (1/2)
    #Round off the result for a more understandable output
    area_print = round(area)
    #Print the area if sides form a triangle
    print("Area of the triangle is", area_print, "square units")

else:
    print("These sides do not form a triangle.")


#Question 4

n=5
#Outer loop
for i in range(n):
    #Inner loop
	    for j in range(i):
	        print ('*', end=" ")
	    print('')
	#Repeated with different step
for i in range(n,0,-1):
	    for j in range(i):
	        print('*', end=" ")
	    print('')


#Question 5      
    
asciichr = 65

# Outer loop for ith rows
for i in range(0,6):
    # Inner loop for jth columns
    for j in range(0,i+1):
        char = chr(asciichr)
        print(char,end="")
        asciichr += 1
    print()


#Question 6   

#Taking upper and lower limit values
lowlimit=int(input("Insert lowlimit limit for range: "))
upperlimit=int(input("Insert upperlimit limit for range: "))

print("Prime numbers between", lowlimit, "and", upperlimit, "are:")

for num in range(lowlimit, upperlimit + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)



#Question 7

#Checking multiples if 7 and divisibility by 11
for i in range(0,500):
    if i%7==0 and i%11==0:
        print(i)
    else:
        continue
    
    
    
#Question 8    

#Creating blank list
Testlist=[]
#Taking 10 values from user
for i in range(10):
    Testlist.append(int(input("Enter number: ")))
    
print(Testlist)

print('''
      Press 1 for positive numbers
      Press 2 for negative numbers
      Press 3 for odd numbers 
      Press 4 for even numbers
      Press 5 for checking frequency of numbers ''',"\n")
      
operation=int(input("Please choose output "))

if operation==1:
    for j in Testlist:
        if j>0:
            print(j)
elif operation==2:
    for j in Testlist:
        if j<0:
            print(j)
elif operation==3:
    #Checking for odd numbers
    for j in Testlist:
        if j%2!=0:
            print(j)
elif operation==4:
    #Checking for even numbers
    for j in Testlist:
        if j%2==0:
            print(j)
elif operation==5:
    #Converting list to dictionary and using count
    Testdic={num:Testlist.count(num) for num in Testlist}
    print(Testdic)
    


#Question 9
#Creating empty list
Testlist=[]
#Taking 10 inputs from user and then adding them to list
for i in range(10):
    Testlist.append(input("Enter word: "))
print(Testlist)
#Converting list to dictionary and then using count 
Testdic={word:Testlist.count(word) for word in Testlist}

print(Testdic)
