# Question_1

def Operations(Expressions):
    a , b  = Expressions.split("+" or '-' or '*' or '/') 
    a , b = float(a) , float(b)
    if '+' in Expressions:
        return a + b
    elif '-' in Expressions:
        return a - b
    elif '*' in Expressions:
        return a * b
    elif '/' in Expressions:
        return a / b
    else:
        return "Invalid Expression"
    
    # expressions = input("Enter the expression: ")
    # print(Operations(expressions))
    
#Question_2

def square(Number):
    return Number ** 2

    # print(square(5))
 
#Question_3

def Typeof(Number):
    if Number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    # print(Typeof(5))

#Question_4

def last_n_elements(n):
    List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    List = list(map(lambda x: x**2, List))
    return List[-n:]
    # print(last_n_elements(5))
 
#Question_5

def Stastical_values(string):
    List = string.split(",")
    List = list(map(int, List))
    print("Mean: ", sum(List)/len(List))
    print("Median: ", List[len(List)//2])
    print("Mode: ", max(set(List), key = List.count))

# string = input("Enter the numbers: ")
# Stastical_values(string)

#Question_6

def balanceFromLog(log):
    balance = 0
    for i in log:
        if "D" in i:
            balance += int(i.strip("D"))
        elif "W" in i:
            balance -= int(i.strip("W"))
    return balance
    #log =  list(input("Enter the log: ").split(","))
    # print(balanceFromLog(log))
    
#Question_7

def sortTuple(List):
    return sorted(List, key=lambda x: (x[0], x[1], x[2]))

print(sortTuple([('tom', 19, 80), ('jhon', 20, 90), ('jony', 17, 93), ('jony', 17, 91), ('json', 21, 85)]))
    