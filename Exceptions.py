#Question_1
def division(a ,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You can't divide by zero"

# print(division(5, 2)) # 2.5
# print(division(5, 0)) # You can't divide by zero

#Question_2
def raiseException(a):
    if a < 0:
        raise ValueError("The value is less than 0")
    return a
def HandleExpcetion(a):
    try:
        return raiseException(a)
    except ValueError as e:
        return e

# print(HandleExpcetion(10)) # The value is less than 0

#Question_3
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

def division(a ,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You can't divide by zero"

# print(division(5, 2)) # 2.5
# print(division(5, 0)) # You can't divide by zero

#Question_4
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(f"The result of division is: {result}")
    finally:
        print("Division operation completed.")
        
divide(5, 2) # The result of division is: 2.5
divide(5, 0) # You can't divide by zero

       

 

 



