# Set a key number.
# Set number of guesses.
# Take a number input from user.
# Print, is the number smaller or greater than the key.
# Print, number of guesses left.
# If number of guesses is over print "game over".

key = 63
chance = 0
guess = 10
print("Game of Guess")
while(chance < guess):
    num = int(input("Enter a number : "))
    if (num>key):
        chance = chance + 1
        if(chance < guess):
            print("Enter smaller number.")
            print("Chances left : ", guess - chance)
        else:
            print("Game over")
        continue
    elif (num<key):
        chance = chance + 1
        if(chance < guess):
            print("Enter greater number.")
            print("Chances left : ", guess - chance)
        else:
            print("Game over.")
        continue
    else:
        print("You won the game.")
        break
    chance = chance + 1
