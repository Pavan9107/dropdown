#Write code to find all duplicate elements in a list.

l = [1,1,1,2,2,2,3,4,5,6]

# for i in l:
#     if l.count(i)== 1:
#         print(i)

n_d=[]
for x in l:
    if x not in n_d:
        n_d.append(x)

print(n_d)
