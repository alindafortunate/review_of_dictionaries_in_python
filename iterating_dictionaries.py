bank_users = {
    "Sarah": 2000,
    "John": 3000,
    "Opio": 4000,
    "Judith": 5000,
}
# Looping to get both the key and the value.
print("Here we get both keys and values.")
for key, values in bank_users.items():
    print(f"Key: {key}, Value: {values}")

# Looping to get only keys.
print()
print("Here we shall only get the keys.")
counter = 0
for key in bank_users.keys():
    counter += 1
    print(f"key{counter}: {key}")

# Default looping returns only the keys.
print()
print("This too only gets the keys.")

counter = 0
for key in bank_users:
    counter += 1
    print(f"key{counter}: {key}")

# Looping for only values.
print()
print("Here we shall only get the values.")
counter = 0
for value in bank_users.values():
    counter += 1
    print(f"Value{counter}: {value}")


# Then for both keys and values.
for key, value in bank_users.items():
    print(f"Key:{key}, Value:{value}")
