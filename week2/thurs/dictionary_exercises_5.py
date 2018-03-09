from operator import itemgetter

def top_three_words(text):
    text = text.lower()
    word_dict = {}
    sorted_words = []
    word_list = text.split(' ')
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sorted_words = sorted(word_dict.items(), key=itemgetter(1), reverse=True)
    top_words = sorted_words[0:3]
    return top_words

if __name__ == "__main__":
    text = input("Please give me a sentence or more: ")
    top_words_list = top_three_words(text)
    print("\nTOP WORDS\n==========")
    for each in top_words_list:
        print(each[0])
    print("==========\n")