list_of_duplicates = [1, 2, 3, 1, 2, 3, 4, 1, 4, 5, 1]
unique_values = []

for i in range(0, len(list_of_duplicates)):
    item = list_of_duplicates.pop(0)
    if item not in unique_values:
        unique_values.append(item)

print(unique_values)