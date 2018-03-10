def file_reader(file):
    with open(file, 'r') as file_handle:
        contents = file_handle.read()
    return(contents)
    
if __name__ == "__main__":
    file_name = input("Please enter a file name: ")
    print(file_reader(file_name))