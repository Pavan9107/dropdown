from logging import lastResort
from operator import index
from os import times

from selenium.webdriver.support.expected_conditions import element_selection_state_to_be

lst = [1, 2, 3, 4, 5]
k =2

def rotate_list(lst, k):
    n = len(lst)
    k = k%n

    for i in range(k):
        last = lst[len(lst)-1]

        for j in range(len(lst)-1,0,-1):
            lst[j] = lst[j-1]

        lst[0]  = last

    return lst

print(rotate_list(lst, k))

# steps:
# remember the last
# shift the elements
# add the last to first index
# repeat k times
