str = "python"
# rev_str = str[::-1]
# print(rev_str)


# rev_str = ""
# for i in range(len(str)-1,-1,-1):
#     rev_str += str[i]
#
# print(rev_str)


rev_str = ""
for i in range(1,len(str)+1):
    rev_str += str[-i]
print(rev_str)

