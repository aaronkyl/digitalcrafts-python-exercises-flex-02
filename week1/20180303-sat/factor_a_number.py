number = int(input("Give me an integer: "))
factors = []

for i in range (1, number + 1):
    if (number / i).is_integer():
        factors.append(i)

print(factors)