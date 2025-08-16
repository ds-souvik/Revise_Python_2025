'''Exercise using dictionary:
Customer Profile Management
You are building a customer profile manager for a CRM (Customer Relationship Management) system. You need to store and manipulate customer data using Python dictionaries.

Tasks:

Create a dictionary named customer with the following fields:

"name": "John Doe"

"age": 32

"city": "New York"

Print the dictionary.

Add "email" and "phone" to the dictionary.

Print the updated dictionary.

Print the customer’s "name" and "city" values.

Check whether the key "email" exists in the dictionary and print the result.

Delete the "age" field from the dictionary.

Print the updated dictionary.

Print all dictionary keys, values, and items.

Remove and print the last inserted key-value pair.

Use .get() to access the key "membership" (which doesn’t exist).

Print the result.

Update the dictionary with a new field "address" set to "221B Baker Street".

Print the final dictionary.'''

customer = {"name": "John Doe", "age": 32, "city": "New York"}
print(f"{customer}")

new_info = dict(email = 'john.doe@example.com', phone = '123-456-7890')
customer.update(new_info)
print(f"{customer}")

print(customer['name'])
print(customer['city'])

print(f"{'email' in customer}")

del customer['age']
print(f"{customer}")

print(f"{customer.keys()}")
print(f"{customer.values()}")
print(f"{customer.items()}")

last_removed_item = customer.popitem()
print(f"{last_removed_item}")

print(f"{customer.get('membership')}")

customer.update({'address': '221B Baker Street'})
print(f"{customer}")