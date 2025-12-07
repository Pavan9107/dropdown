lst = [ 9, 8, 4, 5, 6, 7, 8, 9]

min = lst[0]
for i in lst:
    if i<min:
        min = i
print(min)

max = lst[0]
for i in lst:
    if i>max:
        max = i

print(max)