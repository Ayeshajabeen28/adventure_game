name = input('hey user  Type your name:  ')
print("Welcome", name, "to this adventure!")

answer = input("you are on a dirt road, it has come to an end and you can go left or right which way you could like to go? ").lower()
if answer == "left":
    answer =input("so you choose left..you come to the road side where you can walk around it or cycling around it? type walk to walk around or cycling to cycle: ")
    if answer == "walk":
        print("you walked for many miles,and you lose the game.")
    elif answer =="cycling":
        print("Cycling may help you lose weight,Cycling will help strengthen your legs,and you won the game.")
    else:
         print("not a valid option.You lose.")
elif answer =="right":
    answer = input("so you choose right, you come to bride, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("you go back,and you lose the game.")
    elif answer =="cross":
        print("you cross the bridge and met a stranger. Do you talk to them(yes/no? ")

        if answer == "yes":
            print("you talk to the stranger and they give you price.and you WIN!")

        elif answer == "no":
            print("you ignore the stranger and you LOSS!")
        else:
            print("not a valid option.You lose.")

else:
    print("not a valid option.You lose.")
print("THANK YOU FOR TRYING",name)
