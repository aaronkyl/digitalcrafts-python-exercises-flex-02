class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(self.year, self.make, self.model)
        return
    
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.people_greeted = []
    
    def __str__(self):
        return "Person object:\n  name = {name}\n  email = {email}\n  phone = {phone}\n  friends = {friends}\n  greeting_count ={greeting_count}".format(name=self.name, email=self.email, phone=self.phone, friends=self.friends, greeting_count=self.greeting_count)

    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person.name not in self.people_greeted:
            self.people_greeted.append(other_person.name)
        return
    
    def print_contact_info(self):
        print("{name}'s email: {email}, {name}'s phone number: {phone}".format(name=self.name, email=self.email, phone=self.phone))
        return

    def add_friend(self, friend):
        self.friends.append(friend)
        return

    def num_friends(self):
        print(len(self.friends))
        return
        
    def num_unique_people_greeted(self):
        print(len(self.people_greeted))
        return
    