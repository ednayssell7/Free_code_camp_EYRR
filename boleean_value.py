found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    if value is not 3:
        found = False
    print(found, value)
print('After', found)