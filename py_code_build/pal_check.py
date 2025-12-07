str = "level"

is_palindrome = True
for i in range(len(str)//2):
    if str[i] != str[len(str)-1-i]:
        is_palindrome = False
        break

# After loop
if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")
