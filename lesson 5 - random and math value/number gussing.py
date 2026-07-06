import random
playing = True
number = random.randint(0,9)
print("Welcome to the number guessing game!")
while playing == True:
    guess = int(input("Guess a number between 0 and 9: "))
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        playing = False
    else:
        print("You got it wrong! Try again.")