number_of_coins = 0
response = "yes"

while response == "yes":
    print("You have {} coins.".format(number_of_coins))
    response = input("Do you want another? ")
    number_of_coins += 1

print("Bye")