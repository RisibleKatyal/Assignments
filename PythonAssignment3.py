# Name  : Chinmay Goyal
# SID   : 21107101
# Branch: Mechanical
import math

#Question 1
print('Q1')

n = int(input('Please enter number: '))
print(f'Binary equivalent of {n} is', bin(n)[2:])

#Queation 2
print('Q2')

a = input('Please enter expression: ')
print(a, '=', eval(a))

#Question 3
print('Q3')

n = int(input("Please enter an integer: "))
print('a)', (n + (n + 1)) * (n + 2))
print('b)', n / 2 * (n - 1))
r = int(input('Please enter radius: '))
print('c)', 4 * math.pi * r * r)
a = int(input('Please enter angle 1: '))
b = int(input('Please enter angle 1: '))
print('d)', math.sqrt((r * math.cos(a) * 2) + (r * math.sin(b) * 2)))

x1 = int(input('Please enter x coordinate of first point: '))
y1 = int(input('Please enter y coordinate of first point: '))
x2 = int(input('Please enter x coordinate of second point: '))
y2 = int(input('Please enter y coordinate of second point: '))
print('e)', (y2 - y1) / (x2 - x1))

#Question 4
print('Q4')

print('4.(a)')
for i in range(5):
    print(i)
print('4.(b)')
for i in range(3, 10):
    print(i)
print('4.(c)')
for i in range(4, 13, 3):
    print(i)
print('4.(d)')
for i in range(15, 5, -2):
    print(i)
print('4.(e)')
for i in range(5, 3):
    print(i)

#Question 5
print('Q5')

C = int(input('Enter number of carbon atoms in molecule: '))
H = int(input('Enter number of hydrogen atoms in molecule: '))
O = int(input('Enter number of oxygen atoms in molecule: '))
print('The molecular weight of the compound is ', H * 1.00794 + C * 12.0107 + O * 15.9994)