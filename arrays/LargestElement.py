# You are given a list of integers. Write a Python function that finds and returns the largest element in the list.
# The integers in the list may not be sorted.
# You can assume that the list will not be empty.


def find_largest_element(input_list):
    positional_var = 0
    num = input_list[0]
    while True:
        positional_var += 1
        if input_list[positional_var] > num:
            num = input_list[positional_var]
        if positional_var == len(input_list) - 1:
            print("The largest element in the list is:", num)
            return num


find_largest_element([5, 7, 2, 4, 1, 9, 4, 12, 4, 3, 11])
find_largest_element([15, 13, 14, 5, 8, 3])
