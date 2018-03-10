from dictionary_exercises_3 import letter_histogram
from dictionary_exercises_4 import word_summary
 
if __name__ == "__main__":
    file_name = input("Please enter a file name: ")
    with open(file_name, 'r') as file_handle:
        contents = file_handle.read()
    print("Letter Histogram: ", letter_histogram(contents))
    print("Word Histogram: ", word_summary(contents))