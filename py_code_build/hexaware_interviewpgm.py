l = [1,2,3,4,5]
target = 5

# for i in l:
#     for j in(i+1,len(l)):
#         if i+j == target:
#             print(i,j)


# for i in range(len(l)-1):
#     if l[i] + l[i+1] == target:
#         print(l[i], l[i+1])

seen = set()

for num in l:
    needed = target - num
    if needed in seen:
        print(needed, num)
    seen.add(num)

