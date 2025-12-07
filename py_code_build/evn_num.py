nums = [1, 2, 3, 4, 5, 6]

for i in nums:
    if i%2 == 0:
        print(i, end = " ")

#The reason your code prints each number on a new line is that the default behavior of print()
# in Python is to add a newline (\n) at the end of each call. To print everything on the same line,
# you can use the end parameter of print(). Here's how you can modify your code:

