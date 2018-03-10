def word_summary(text):
    text = text.lower()
    word_dict = {}
    word_list = text.replace('\n', ' ').replace('.', ' ').split(' ')
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

if __name__ == "__main__":
    text = input("Please give me a sentence or more: ")
    print(word_summary(text))