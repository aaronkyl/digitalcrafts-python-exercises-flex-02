def file_reader(file):
    file_handle = open(file, 'r')
    contents = file_handle.read()
    file_handle.close()
    
    print(contents)
    
if __name__ == "__main__":
    file_name = input("Please enter a file name: ")
    file_reader(file_name)
