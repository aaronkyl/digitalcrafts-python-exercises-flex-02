# have simple dictionary that serves as phonebook (no objects)
# person's name is the key
# person's phone number is the value
# store phonebook in file

import pickle

phonebook = {}

def print_menu():
    print('')
    print('Electronic Phone Book')
    print('=====================')
    print('1. Look up an entry')
    print('2. Set an entry')
    print('3. Delete an entry')
    print('4. List all entries')
    print('5. Quit')
    
def lookup_contact():
    name = input("Name of contact: ").title()
    if name in phonebook:
        print("{}'s number: {}".format(name, phonebook[name]))
    else:
        print("{} not found".format(name))
    return

def create_contact():
    name = input("Name of contact to add: ").title()
    if name in phonebook:
        print("Contact with name of {} already exists.".format(name))
    else:
        phonenumber = ''
        print("Number must include area code and consist only of numeric characters.")
        while len(phonenumber) != 10:# and not phonenumber.isnumeric():
            phonenumber = input("Number: ")
        phonebook[name] = phonenumber
    return
    
def delete_contact():
    name = input("Name of contact to delete: ").title()
    if name in phonebook.keys():
        del phonebook[name]
        print("Deleted entry for {}".format(name))
    else:
        print("{} not found".format(name))
    return

def list_all_contacts():
    if not len(phonebook):
        print("Phonebook is empty.")
    else:
        for k,v in phonebook.items():
            print("{}: {}".format(k.title(), v[:3] + '-' + v[3:6] + '-' + v[6:]))
    return
        
if __name__ == "__main__":
    while True:
        print_menu()
        while True:
            try:
                user_selection = int(input("What do you want to do (1-5)? "))
                break
            except ValueError:
                print("Invalid option. Please try again.")
        if user_selection < 1 or user_selection > 5:
            print("Invalid option. Please try again")
        elif user_selection == 1:
            lookup_contact()
        elif user_selection == 2:
            create_contact()
        elif user_selection == 3:
            delete_contact()
        elif user_selection == 4:
            list_all_contacts()
        elif user_selection == 5:
            break
            