conversions = (('A', '4'), ('E', '3'), ('G', '6'), ('I', '1'), ('O', '0'), ('S', '5'), ('T', '7'))

plaintext = input("Give me a paragraph! ")

result = plaintext.upper()

for i in range(0, len(conversions)):
    result = result.split(conversions[i][0])
    result = conversions[i][1].join(result)

print(result.lower())