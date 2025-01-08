inventory = {
    "apples": 10,
    "bananas": 15,
    "oranges": 5,
    "grapes": 20,
}

# Adding items to the invetory dict using, (key and value)
inventory["mangoes"] = 20
inventory["pawpaws"] = 15

# print(inventory)

# new dictionary
new_dictionary = dict()


# Creating keys.
age = 26
colors = ("red", "blue", "yellow")
name = "Alinda"
city = "Kampala"
new_dictionary[age] = "Fortunate"
new_dictionary[colors] = "RBY"
new_dictionary[name] = "Fortunate"
new_dictionary[city] = "Uganda"

# Possible datatypes for dictionary keys (numerical values, strings, tuples)
# Modfying values within the python dictionary.
new_dictionary[city] = "Uganda's city"
new_dictionary[name] = "Fortunate is the second name of Alinda."
# print(new_dictionary)

# Accessing values.
bank_users = {
    "Akello": 2000,
    "Opio": 3000,
    "Okello": 4000,
    "John": 5000,
}

# To get the balance of John.
john_balance = bank_users["John"]
opio_balance = bank_users["Opio"]

bank_users["John"] = john_balance - 1000
print(f"John's balance: {john_balance} UGX ")
print(f"Opio's balance: {opio_balance} UGX ")

del bank_users["Okello"]
print(bank_users)
