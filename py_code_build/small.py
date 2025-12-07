numbers = [3, 7, 2, 9, 4]
small = numbers[0]

for i in numbers:
    if i < small:
        small = i

print(small)