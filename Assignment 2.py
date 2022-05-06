given="Python is a case sensitive language"
ap=len(given)
bp=given[::-1]
cp=given[10:26]
dp=given.replace("a case sensitive","object oriented")
ep=given.find("a")
fp=given.replace(" ","")
print("Question 1 option a is", ap)
print("Question 1 option b is", bp)
print("Question 1 option c is", cp)
print("Question 1 option d is", dp)
print("Question 1 option e is", ep)
print("Question 1 option f is", fp)



name="Chinmay Goyal"
sid="21107101"
dept="Mechanical Engineering"
cgpa="9.0"
print("hey, ",name," here!","\n","My SID is ",sid,"\n","I am from",dept,"department and my CGPA is",cgpa)



a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print(a>>2)
print(b>>2)
print(a<<2)
print(b<<4)


subtle=input("Enter string: ")
subs="name"
if subs in subtle:
  print("Yes")
else:
  print("No")



side1 = float(input("Enter length 1\n"))
side2 = float(input("Enter length 2\n"))
side3 = float(input("Enter length 3\n"))

side_1 = int(round(side1))
side_2 = int(round(side2))
side_3 = int(round(side3))

a = side_1 + side_2
b = side_2 + side_3
c = side_1 + side_3

check_1 = a > side_3
check_2 = b > side_1
check_3 = c > side_2

answer = str(check_1 & check_2 & check_3)
answer = answer.replace("True", "Yes")
answer = answer.replace("False", "No")

print("Can the given input lengths form a triangle?")
print(answer)



n_1 = int(input("Enter 1st number (a) "))
n_2 = int(input("Enter 2nd number (b) "))
ex_or = n_1 ^ n_2
bin_exor = bin(ex_or)
check_string = str(bin_exor)
bits_need_flip = check_string.count("1")
print("Number of bits needed to be flipped to convert ‘a’ to ‘b’ are:", bits_need_flip)
