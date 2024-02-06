def RootsOfQuatratic(a,b,c):
    D = b**2 - 4*a*c
    if D > 0:
        print('the roots are : ' , (-b + D**0.5)/(2*a) , (-b - D**0.5)/(2*a))
        return "Real and Distinct Roots"
    elif D == 0:
        print('the roots are : ' , (-b + D**0.5)/(2*a) , (-b - D**0.5)/(2*a))
        return "Real and Equal Roots"
    else:
        return "Imaginary Roots"

# print(RootsOfQuatratic(1,2,1))

def CafeMenu(choice):
    if choice == 1:
        return "One Soup and salad coming right up! "
    elif choice == 2:
        return "One Pasta with meat sauce coming right up! "
    elif choice == 3:
        return "One Chef's Special coming right up! "
    else:
        return " Sorry, that is not a valid choice."

# print("Welcome to the cafe! Which choice would you like to order? ")
# choice = int(input("1. Soup and salad \n2. Pasta with meat sauce \n3. Chef's Special \n"))
# print(CafeMenu(choice))