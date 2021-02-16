# Number of chances = 10
# Use while loop
# Game - Rock, Paper, Scissor
import random
n = 0
turn = 10
comp_tot = 0
usr_tot = 0
print("Rock - Paper - Scissor")
print("Rock -----> r")
print("Paper -----> p")
print("Scissor -----> s")
print("User will play first.")
while n < 10:
    print("User : ")
    user = input()
    if user == "r":
        list1 = ["r", "p", "s"]
        choice = random.choice(list1)
        print("Computer : ", choice)
        if choice == "p":
            print("Computer wins.")
            comp_tot = comp_tot + 1
            turn = turn - 1
            print("Computer Points : ",comp_tot)
            print("Turns left : ", turn)
        elif choice == "s":
            print("User wins.")
            usr_tot = usr_tot + 1
            turn = turn - 1
            print("User Points : ", usr_tot)
            print("Turns left : ", turn)
        else:
            print("Tie.")
            turn = turn - 1
            print("Turns left : ", turn)
    elif user == "p":
        list1 = ["r", "p", "s"]
        choice = random.choice(list1)
        print("Computer : ", choice)
        if choice == "r":
            print("User wins.")
            usr_tot = usr_tot + 1
            turn = turn - 1
            print("User Points : ", usr_tot)
            print("Turns left : ", turn)
        elif choice == "s":
            print("Computer wins.")
            comp_tot = comp_tot + 1
            turn = turn - 1
            print("Computer Points : ", comp_tot)
            print("Turns left : ", turn)
        else:
            print("Tie.")
            turn = turn - 1
            print("Turns left : ", turn)
    elif user == "s":
        list1 = ["r", "p", "s"]
        choice = random.choice(list1)
        print("Computer : ", choice)
        if choice == "p":
            print("User wins.")
            usr_tot = usr_tot + 1
            turn = turn - 1
            print("User Points : ", usr_tot)
            print("Turns left : ", turn)
        elif choice == "r":
            print("Computer wins.")
            comp_tot = comp_tot + 1
            turn = turn - 1
            print("Computer Points : ", comp_tot)
            print("Turns left : ", turn)
        else:
            print("Tie.")
            turn = turn - 1
            print("Turns left : ", turn)
    else:
        print("Invalid Input.")
        turn = turn - 1
        print("Turns left : ", turn)
    n = n + 1
print("-------------------------------------------------------------------------------------------")
if usr_tot>comp_tot :
    print("User wins the match.")
elif usr_tot<comp_tot :
    print("Computer wins the match.")
else:
    print("Match ties.")