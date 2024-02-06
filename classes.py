#question_1
import random
#overloading
# In general python doesnt support overloading but we can achieve it by using default arguments.

#overriding

class Parent():
    def show(self):
        print("Parent")
class Child(Parent):
    def show(self):
        print("Child")
        super().show()

# obj = Child()
# obj.show()

#question_2

import random

class Player:
    def __init__(self, name):
        self.name = name

    def guess(self):
        x = input(f"{self.name}, guess a number between 0 and 9: ")
        return int(x)

class GuessGame:
    def __init__(self):
        self.players = [Player("Mandy"), Player("Phani"), Player("Himadri")]
        self.number = random.randint(0, 9)

    def startGame(self):
        print("Welcome to Guess Game!")
        print("I'm thinking of a number between 0 and 9...")

        winners = []   

        for player in self.players:
            guess = player.guess()
            print(f"{player.name} guessed {guess}")

            if guess == self.number:
                winners.append(player.name)  

        if winners:
            print("The winner(s) is/are:")
            for winner in winners:
                print(winner)
        else:
            print("No one guessed it right. The number was " + str(self.number))
class GameLauncher:
    @staticmethod
    def main():
        game = GuessGame()
        game.startGame()

# # Start the game
# GameLauncher.main()


#question_3
 
import math
class Quadrilateral():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def __str__(self):
        return f'({self.x1}, {self.y1}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3}), ({self.x4}, {self.y4})'

    def angle_between_sides(self):
        # Calculate vectors for each pair of consecutive sides
        vector1 = (self.x2 - self.x1, self.y2 - self.y1)
        vector2 = (self.x3 - self.x2, self.y3 - self.y2)
        vector3 = (self.x4 - self.x3, self.y4 - self.y3)
        vector4 = (self.x1 - self.x4, self.y1 - self.y4)

        # Calculate angles using the dot product and cross product
        angle1 = math.degrees(math.atan2(vector1[1], vector1[0]) - math.atan2(vector4[1], vector4[0]))
        angle2 = math.degrees(math.atan2(vector2[1], vector2[0]) - math.atan2(vector1[1], vector1[0]))
        angle3 = math.degrees(math.atan2(vector3[1], vector3[0]) - math.atan2(vector2[1], vector2[0]))
        angle4 = math.degrees(math.atan2(vector4[1], vector4[0]) - math.atan2(vector3[1], vector3[0]))

        # Normalize angles to be in the range [0, 360)
        angle1 = round((angle1 + 360) % 180 ,2)
        angle2 = round((angle2 + 360) % 180 ,2)
        angle3 = round((angle3 + 360) % 180 ,2)
        angle4 = round((angle4 + 360) % 180 ,2)
           

        return angle1, angle2, angle3, angle4
    
class Trapezoid(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)

    def area(self):
        parallel_side1 = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        parallel_side2 = math.sqrt((self.x4 - self.x3)**2 + (self.y4 - self.y3)**2)
        height = abs(self.y2 - self.y1)  # Assuming one of the sides is parallel to the x-axis
        return (parallel_side1 + parallel_side2) * height / 2

    
class Parallelogram(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)

    def area(self):
        base = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        height = abs(self.y2 - self.y1)  # Assuming one of the sides is parallel to the x-axis
        return base * height
    
    
class Rectangle(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)

    def area(self):
        length = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        width = abs(self.y2 - self.y1)  # Assuming one of the sides is parallel to the x-axis
        return length * width


class Square(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)

    def area(self):
        side_length = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return side_length**2



print("Square :")
squ = Square(1,1,1,-1,-1,-1,-1,1)
print(squ.area())
print(squ.angle_between_sides())      

print("Rectangle :")
rect = Rectangle(1,1,1,-1,-1,-1,-1,1)
print(rect.area())
print(rect.angle_between_sides())
      
