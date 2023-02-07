# Create by Andrew Bienvenue
#The lucky number guessing game
#The user is going to guess a random number from 0 to 100
#The program is going to keep track of the attempt

# Importing the random module
import random


#Generating the random number
lucky_number = random.randrange(0,100)

# Displaying a welcome message
message = "Welcome to a Lucky number guessing game!"
message2 = "You have 3 tries to guess today's lucky number!"
print(message, message2)

# implementing a try condition to check if the user enter a number instead a string or integer
while True:

    try:
        count = 0    # initialing the count value

        while count < 6:
            count += 1

            #Getting user input
            number = input("Guess today's lucky number between 0 to 100: \n")
            number_int = int(number)

            # using a decision condition to check the user input
            if number_int == lucky_number:
                break

            elif number_int  < lucky_number:
                print(f"You guessed too small, try again")

            else:
                print(f"You guessed too high, try again")

        if number_int == lucky_number:
            print(f"Congratulation you guess today's lucky number: {lucky_number} and you guess it in {count} try")
            break    # breaking from the loop

        else:
            print(f"Sorry, you didn't guess today's lucky number and the lucky number is {lucky_number}")

            break   # breaking from the loop

    # implementing an exception for the user input
    except Exception:
        print("You Enter a string instead an Integer:\nPlease reenter the lucky number:")
