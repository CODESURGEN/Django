import itertools 
#Question_1
import math
def Power_and_Squareoot(x,y,z):
    print("The power of ", x, "to the ", y, "is ", pow(x,y))
    print("The square root of ", z, "is ",math.sqrt(z))
    
# Power_and_Squareoot(2,3,4)
#Question_2

    # Elements = {"A","B","C","D","E"}
    # No_of_elements = 3
    # print(list(itertools.combinations(Elements, No_of_elements)))
    # print(len(list(itertools.combinations(Elements, 3))))     #5c3 = 10
 
#Question_3

def Unique_List(Duplicate_list):
    return list(set(Duplicate_list))
    # print(Unique_List([1,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]))

#Question_4
def addition(*args):
    print(sum(args))

# addition(1, 2, 3, 4, 5)  # Outputs: 15

#Question_5

def func1(x,y):
    lis =[]
    if x%2 == 0:
        for i in range(x+2, y,2):
            lis.append(i)
    else:
        for i in range(x+1, y,2):
            lis.append(i)
    return lis
# print(func1(2, 50))

#Question_6
# recusive function

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
# print(fibonacci(10))

def getEvenNumbers(Numbers):
    return list(filter(lambda x: x%2 == 0, Numbers))

print(getEvenNumbers([1,2,3,4,5,6,7,8,9,10]))
    
 
    
 
 