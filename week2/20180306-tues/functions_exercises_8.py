def play_again():
    answer = input("Do you want to play again (Y or N)? ")
    if answer.lower() is 'y':
        return True
    else:
        return False

if __name__ == "__main__":
    play_again()