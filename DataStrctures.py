#question 1

    # Postive_Numbers = []
    # for i in range(1, 11):
    #     a = int(input("Enter a number: "))
    #     Postive_Numbers.append(a)
    # Postive_Numbers.sort(reverse=True)
    # print(Postive_Numbers)

#question 2

Nofclasses = int(input("How many classes did you take? "))
ReportCard = {}
for i in range(1, Nofclasses + 1):
    Nameofclass = str(input("What was the name of the class? "))
    Grade =   int(input("What was your grade? "))
    ReportCard[Nameofclass] = Grade
print("Your report card is:")
for i in ReportCard:
    print(i, ":", ReportCard[i])
