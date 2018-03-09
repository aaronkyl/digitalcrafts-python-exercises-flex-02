ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

email = ramit['email']
first_interest = ramit['interests'][0]
for friend in ramit['friends']:
  if friend['name'] == "Jasmine":
    jasmine_email = friend['email']
for friend in ramit['friends']:
  if friend['name'] == "Jasmine":
    jasmine_second_interest = friend['interests'][1]

print(email)
print(first_interest)
print(jasmine_email)
print(jasmine_second_interest)