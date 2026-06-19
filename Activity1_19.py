import random
playing = True
number = (random.randint(0,9))

print("I will generate a number from 0 to 9 and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")


while playing:
    guess = int(input("Give me you best guess! \n"))
    if number == guess:
        print("OMG YOU JUST WON THE GAME OF THE CENTURY!!")
        print("The number was", number,"good job.")

    else:
        print("Your guess isn't right, try again.\n")