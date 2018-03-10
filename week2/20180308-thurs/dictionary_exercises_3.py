def letter_histogram(word):
    word = word.lower()
    letter_dict = {}
    for char in word:
        if char.isalpha():
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
    return letter_dict
    
if __name__ == "__main__":
    word = input("Give me a word: ")
    print(letter_histogram(word))
    