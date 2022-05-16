name = input("Type in your name: ")
print(f"Welcome {name} to this adventure! \nYour aim is to find the gold. Let's get started.")

answer_1 = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer_1 == "left":
    
    answer_2 = input("You came to a river, do you want to walk around or swim across the river? (Choose walk/swim) ").lower()
    if answer_2 == "swim":
        print("You swam across and unfortunately, was eaten by an alligator.")
    elif answer_2 == "walk":
        print("You walked for many hours, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer_1 == "right":
    answer_3 = input("You come to a bridge. It looks wobbly, do you want to cross it or head back? (Choose cross/back) ").lower()
    if answer_3 == "back":
        print("You go back and lose.")
    elif answer_3 == "cross":
        answer_4 = input("You cross the bridge and meet the stranger. Do you talk to him? (Choose yes/no) ")
        if answer_4 == "yes":
            print(f"You talked to the stranger and they gave you gold. Congratulations {name}, you WIN!")
        elif answer_4 == "no":
            print("You ignore the stranger and do not receive the gold. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print(f"Thank you {name} for playing the game. I hope that you enjoyed it!")