# initialize variables
plaintext = ''
key = -1

# get plaintext and cipher value from user
while plaintext == '':
    plaintext = input("Please enter your text: ")
while key < 0:
    key = int(input("Please enter a non-negative integer key: "))

# prepare output line
print("ciphertext: ", end='')

# iterate through plaintext
for char in plaintext:
    if char.isalpha():
        # flag to record case of current character
        if char.isupper():
            a = 'A'
        else:
            a = 'a'
        # encode current alpha character and print it
        print(chr((((ord(char) - ord(a)) + key) % 26) + ord(a)), end='')
    else:
        # print non-alpha character
        print(char, end='')

# print newline at end
print('')
        