# # Exercise 1: Create a list to store names of your favorite fruits.
# # Write code to access the second element and print it.

# my_fruits = ["apples", "mangoes", "pineapples"]
# second_element = my_fruits[1]
# # print(f"The second element is {second_element}")


# # Exercise 2: Define a dictionary to store information about your favorite book,
# # including title, author, and genre. Use the method to retrieve the genre.
# my_dictionary = {
#     "title": "Purpose Driven Life.",
#     "author": "Rick Warren",
#     "genre": "spirituality",
# }

# # print(my_dictionary["genre"])


# # Exercise 3: Write a program to generate a random set of numbers between 1 and 10.
# # Use set operations to remove duplicates and display the unique numbers.
import random

unique_numbers = set()

for number in range(20):
    number = random.randint(1, 10)
    unique_numbers.add(number)

print(f"The set of numbers is betwee 1 and 10 is: {unique_numbers}")
print()

# Exercise 3: Write a program to generate a random set of numbers between 1 and 10.
# # Use set operations to remove duplicates and display the unique numbers.

# Better code


import random

random_numbers = []
for _ in range(20):
    random_values = random.randint(1, 10)
    random_numbers.append(random_values)

print(random_numbers)
unique_values = set(random_numbers)
print()
print(unique_values)

# Creating a set
# Use a constructor
