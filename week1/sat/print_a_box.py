height = int(input("Height? "))
width = int(input("Width? "))

for i in range(0, height):
    if i == 0 or i == height - 1:
        print('*' * width)
    else:
        for j in range(0, width):
            if j == 0 or j == width - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print('')