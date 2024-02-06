# Assignment -2  Question 1
    # x1,y1,r1 = input("Enter the center and radius of the circle: ").split(" ")
    # x2,y2,r2 = input("Enter the center and radius of the circle: ").split(" ")
    # x1,y1,r1 = float(x1),float(y1),float(r1)
    # x2,y2,r2 = float(x2),float(y2),float(r2)


    # distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

    # if distance < r1+r2:
    #     print("The balls are  colliding")
    # else:
    #     print("The balls are not colliding")

# Assignment -2  Question 2

def pig_latin_converter(word):
    vowels = ['a','e','i','o','u']
    if word[0] in vowels:
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"

sting = input("Enter the string: ")
words = sting.split(" ")
for word in words:
    print(pig_latin_converter(word),end=" ")

