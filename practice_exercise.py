# Exercise 1: Create a list to store names of your favorite fruits.
# Write code to access the second element and print it.

my_fruits = ["apples", "mangoes", "pineapples"]
second_element = my_fruits[1]
# print(f"The second element is {second_element}")


# Exercise 2: Define a dictionary to store information about your favorite book,
# including title, author, and genre. Use the method to retrieve the genre.
my_dictionary = {
    "title": "Purpose Driven Life.",
    "author": "Rick Warren",
    "genre": "spirituality",
}

# print(my_dictionary["genre"])


# Exercise 3: Write a program to generate a random set of numbers between 1 and ten.
# Use set operations to remove duplicates and display the unique numbers.
import random

# Empty set
set1 = set()

for i in range(10):
    number = random.randint(1, 10)
    set1.add(number)
print(f"The set of numbers is betwee 1 and 10 is: {set1}")
