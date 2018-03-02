import random
secret_number = random.randint(1, 10)
guesses_left = 5
guess = 0

print("I am thinking of a number between 1 and 10.")

while guesses_left:
    guesses_left -= 1
    guess = int(input("What's the number? "))
    if guess < secret_number:
        print("{guess} is too low.".format(guess=guess))
    elif guess > secret_number:
        print("{guess} is too high.".format(guess=guess))
    else:
        print("Yes! You win!")
        break

if not guesses_left:
    print("You ran out of guesses!")