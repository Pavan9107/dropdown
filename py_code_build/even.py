from selenium.webdriver.common.devtools.v140.fetch import continue_request

numbers = [3, 7, 2, 9, 4]
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)

print(even)


even_com = [i for i in numbers if i%2==0]