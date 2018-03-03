height = int(input("Height: "))

for i in range(0, height):
    print(' ' * (height - 1 - i), end='')
    print('*' * (i * 2 + 1))