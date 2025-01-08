# Practicing operations on a list.
# Indexing
my_list = [10, 20, 30, 40, 50]
# print(my_list[0])

# slicing.
# What it is: Slicing allows you to extract sub-lists from a list using start, stop, and step indices.
# How it works:

# # # You use the syntax list[start:stop:step] to slice a list.

# The start index is inclusive, the stop index is exclusive, and step is the interval between elements.
# first_three_items = my_list[:3]
# print(first_three_items)

# # using my_list[start:stop:step]
my_list1 = [1, 2, 3, 4, 5, 6]
# even_items = my_list1[1:6:2]
# print(even_items)

# first_four_item = my_list1[:4]
# print(first_four_item)

# reversed_list = my_list1[::-1]
# print(reversed_list)

# Appending
# Refers to adding elements to the end of the list.
# syntax, your append() to add elemets to the end of the list.
add_7 = my_list1.append(7)
# print(my_list1)

# Removing.
# Removing is deleting elements from a list.
# we use remove()
remove_4 = my_list1.remove(4)
print(my_list1)
