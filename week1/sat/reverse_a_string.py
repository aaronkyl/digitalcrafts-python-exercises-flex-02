original_string = input("Give me a string! ")

#for i in range(len(original_string), 0, -1):
#    print(original_string[i-1], end='')
#    
#print('')

# Alternate method using extended slice

print(original_string[::-1])