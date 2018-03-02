secret_number = 5

print("I am thinking of a number between 1 and 10.")

guess = int(input("Whats the number? "))

while guess != secret_number:
    print("Nope, try again.")
    guess = int(input("Whats the number? "))
    
print("Yes! You win!")