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
    print('5. Save entries')
    print('6. Load saved entries')
    print('7. Quit')

def print_contact_info(name):
    print("{}'s Information".format(name))
    print("   Phone: {}".format(phonebook[name]['phonenumber']))
    print("   Email: {}".format(phonebook[name]['email']))
    print("   Website: {}".format(phonebook[name]['website']))

    
def lookup_contact():
    name = input("Name of contact: ").title()
    if name in phonebook:
        print_contact_info(name)
    else:
        print("{} not found".format(name))
    return

def create_contact():
    name = input("Name of contact to add: ").title()
    if name in phonebook:
        print("Contact with name of {} already exists.".format(name))
    else:
        phonebook[name] = {}
        phonenumber = ''
        print("Number must include area code and consist only of numeric characters.")
        while len(phonenumber) != 10 or not phonenumber.isnumeric():
            phonenumber = input("Number: ")
        email = input("Email: ")
        website = input("Website: ")
        phonebook[name]['phonenumber'] = phonenumber[:3] + '-' + phonenumber[3:6] + '-' + phonenumber[6:]
        phonebook[name]['email'] = email
        phonebook[name]['website'] = website
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
        for contact in phonebook.keys():
            print_contact_info(contact)
    return

def save_entries():
    if len(phonebook):
        phonebook_file = open('phonebook.pickle', 'wb')
        pickle.dump(phonebook, phonebook_file)
        phonebook_file.close()
    else:
        print("Nothing in phonebook to save.")
    return
    
def load_saved_entries():
    phonebook_file = open('phonebook.pickle', 'rb')
    phonebook = pickle.load(phonebook_file)
    phonebook_file.close()
    return phonebook
        
if __name__ == "__main__":
    while True:
        print_menu()
        while True:
            try:
                user_selection = int(input("What do you want to do (1-7)? "))
                break
            except ValueError:
                print("Invalid option. Please try again.")
        if user_selection < 1 or user_selection > 7:
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
            save_entries()
        elif user_selection == 6:
            try:
                phonebook = load_saved_entries()
            except FileNotFoundError:
                print("No saved phonebook to load.")
        elif user_selection == 7:
            break
            