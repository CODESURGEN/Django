Total_No_of_stones = 10
Max_pick = 5

while Total_No_of_stones > 0:
    print("There are ", Total_No_of_stones, "stones left")
    pick = int(input("How many stones would you like to pick? "))
    if pick > Max_pick or pick < 1:
        print("You can only pick 1 to 5 stones")
    else:
        Total_No_of_stones -= pick
        if Total_No_of_stones <= 0:
            print("You lost!")
        else:
            print("There are ", Total_No_of_stones, "stones left")
            pick = 5 - pick
            Total_No_of_stones -= pick
            if Total_No_of_stones <= 0:
                print("You won!")
            else:
                print("Computer picks ", pick, "stones")
print("Game over!")