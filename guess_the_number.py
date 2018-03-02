import random
secret_number = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")

guess = int(input("Whats the number? "))

while guess != secret_number:
    if guess < secret_number:
        print("{guess} is too low.".format(guess=guess))
    else:
        print("{guess} is too high.".format(guess=guess))
    guess = int(input("Whats the number? "))
    
print("Yes! You win!")