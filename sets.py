set1 = {"apples", "oranges", "pineapples"}
set2 = {"mangoes", "bananas", "lemons", "apples"}

# Using the union method.
# Combines two sets to create a new set containing all unique elements from both sets.
union_of_set1_and_set2 = set1.union(set2)
print(union_of_set1_and_set2)


# Using the intersection method.
# Finds the common elements between two sets.
intersection_of_set1_and_set2 = set2.intersection(set1)
print(intersection_of_set1_and_set2)


# Using the difference() method.
# Finds the elements present in one set but not in another set.

difference_between_set1_and_set2 = set1.difference(set2)
print(difference_between_set1_and_set2)


# print(type(set1))
# print(dir(set1))
