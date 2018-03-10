from dictionary_exercises_3 import letter_histogram
from dictionary_exercises_4 import word_summary
 
if __name__ == "__main__":
    file_name = input("Please enter a file name: ")
    file_handle = open(file_name, 'r')
    contents = file_handle.read()
    print("Letter Histogram: ", letter_histogram(contents))
    print("Word Histogram: ", word_summary(contents))
    file_handle.close()