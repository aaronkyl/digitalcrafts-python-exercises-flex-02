secret_number = 5

print("I am thinking of a number between 1 and 10.")

while guess != secret_number:
    guess = int(input("Whats the number? "))
    
print("Yes! You win!")
