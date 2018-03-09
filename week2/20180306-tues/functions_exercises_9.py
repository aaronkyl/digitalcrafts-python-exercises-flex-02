def play_again():
    while True:
        answer = input("Do you want to play again (Y or N)? ")
        if answer is 'Y':
            return True
        elif answer is 'N':
            return False
        else:
            print("Invalid response!")

if __name__ == "__main__":
    play_again()