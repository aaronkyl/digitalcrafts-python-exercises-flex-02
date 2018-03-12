class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print("{}'s email is {} and phonenumber is {}".format(sonny.name, sonny.email, sonny.phone))
print("{}'s email is {} and phonenumber is {}".format(jordan.name, jordan.email, jordan.phone))