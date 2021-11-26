import random
min=1
max=6
n=input(("Do you want to roll?(y/n):"))
while n=='Y' or n=='y':
    num=(random.randint(1,6))
    print("YOU ROLLED A:", num)
    if num == 1:
        print("_" * 7)
        print(" " * 11)
        print(" "*5, "*", " " * 5)
        print(" " * 11)
        print("_" * 7)
    elif num == 2:
        print("_" * 7)
        print("*")
        print(" " * 11)
        print(" "*10, "*")
        print("_" * 7)
    elif num == 3:
        print("_" * 7)
        print("*")
        print(" "*5, "*", " " * 5)
        print(" "*10, "")
        print("_" * 7)
    elif num == 4:
        print("_" * 7)
        print("*", " " * 9, "*")
        print(" " * 11)
        print("*", " " * 9, "*")
        print("_" * 7)
    elif num == 5:
        print("_" * 7)
        print("*", " " * 9, "*")
        print(" "*5, "*", " " * 5)
        print("*", " " * 9, "*")
        print("_" * 7)
    elif num == 6:
        print("_" * 7)
        print("*", " " * 9, "*")
        print("*", " " * 9, "*")
        print("*", " " * 9, "*")
        print("_" * 7)
    n=input("Do you want to roll the die again?:")