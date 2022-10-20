#Chinmay Goyal
#Mechanical
#21107101

#In-place algorithms are the ones which now new variables are introduced for the operation of the algorithm.
#Out-place algorithms introduce new variables to operate. For example, a function to swap two numbers can be made in two ways:

# swap(a,b):
#   c = a
#   a = b
#   b = c

#This is an out-place algorithm as it introduced the variable c.

#Another method might be

# swap(a,b):
#   a = a + b
#   b = a - b
#   a = a - b


def InsertionSort(arr = []):
    for x in range(1,len(arr)):
        ExtractedElement = arr[x]
        for j in range(x-1,-1,-1):
            if arr[j]>ExtractedElement: 
                arr[j+1] = arr[j] 
                arr[j] = ExtractedElement
    return arr



#Sample Array
import random
Question_List = random.sample(range(0,100),50)

print(Question_List)
print(InsertionSort(Question_List))
