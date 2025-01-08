empty_dict = dict()
# print(empty_dict)

food_items = {
    "food": [
        "matooke",
        "cassava",
        "potatoes",
    ],
    "vegetables": [
        "oranges",
        "apples",
        "guavas",
    ],
    "drinks": [
        "soda",
        "juice",
        "tea",
    ],
}
# print(type(food_items))
# dict methods.

# get(key, default): This method retrieves the value associated with a specified key in the dictionary.
# If the key is not found, it returns the default value (if provided) or None.
result = food_items.get("vegetables", "quavas")
# print(result)

result1 = food_items.get("drinks")
# print(result1)
result2 = food_items.get("home", "tea")
# print(result2)

# keys(): This method returns a view object that contains all the keys in the dictionary,
#  allowing you to iterate over them

all_keys = food_items.keys()
# print(all_keys)

contents_in_food_key = food_items.get("food")
# print(contents_in_food_key)

# values(): Similar to keys(),
# this method returns a view object that contains all the values in the dictionary.
values_in_food_items = food_items.values()
# print(values_in_food_items)

# items(): This method returns a view object that contains tuples of key-value pairs,
# allowing you to iterate over them together.

items_in_food_key = food_items.items()
print(items_in_food_key)
