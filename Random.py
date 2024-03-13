import random
num = random.randint(1, 100)
guess = -1  
while guess != num:
    guess_str = input("Enter your guess: ")
    guess = int(guess_str)

    if guess < num:
        print("Too low, try again.")
    elif guess > num:
        print("Too high, try again.")

print("You guessed the number",num,"correctly!")