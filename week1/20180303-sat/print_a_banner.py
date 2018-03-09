text = input("Text? ")
banner_width = len(text) + 4

for i in range(0, 3):
    if i == 0 or i == 2:
        print('*' * banner_width)
    else:
        for j in range(0, 5):
            if j == 0:
                print('*', end='')
            elif j == 1 or j == 3:
                print(' ', end='')
            elif j == 4:
                print('*')
            else:
                print(text, end='')