vowels = ('a', 'e', 'i', 'o', 'u')

word = input("Give me a word! ")
result = ""

for i in range(0, len(word)):
    if word[i] in vowels and word[i] == word[i-1]:
        result = result + (word[i] * 4)
    else:
        result = result + word[i]
    
print(result)