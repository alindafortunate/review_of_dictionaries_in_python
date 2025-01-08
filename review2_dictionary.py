bank_users = {
    "Sarah": 2000,
    "John": 3000,
    "Opio": 4000,
    "Judith": 5000,
}

selcted_choice = bank_users["Opio"]
print(selcted_choice)
print(bank_users.get("Sarah"))

# Two methods can be used to get the bank_user's balance.
# Method 1
balance_sarah = bank_users["Sarah"]
print(f"Sarah's balance: {balance_sarah} UGX")

# Ideally method 1 is better since it raises a Keyerror incase of the incorrect key used.
# Method 2
sarah_balance = bank_users.get("Sarah", "Key does not exist.")
print(f"Sarah's balance: {sarah_balance} UGX")

print(bank_users.items())


# Working with clear and copy methods

# bank_users.clear()
bank_user = bank_users.copy()
print(bank_users)
print(bank_user)
