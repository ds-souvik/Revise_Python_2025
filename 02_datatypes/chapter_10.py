'''Operations on dictionaries'''

#Ways of defining lists

# 1. Simple definition

tel = {'Souvik': 30, 'Sayli': 31}
print(f"{tel}")

tel = dict(Souvik = 30, Sayli = 31)
print(f"{tel}")

tel = dict([('Souvik', 30), ('Sayli', 31)])
print(f"{tel}")

new_tel = {x: x**2 for x in (2,3,4)}
print(f"{new_tel}")

#Delete a component in the dictionary
del new_tel[2]
print(f"{new_tel}")

login_info = dict(customer_name = "Souvik", customer_id = 2431, customer_age = 30, customer_birth_place = "Gujarat", 
                  interest = "Machine Learning")
print(f"{login_info}")

#Membership testing
print(f"Do we have customer birth place: {'customer_birth_place' in login_info}")

#Check keys, values and items
print(f"Get login keys: {login_info.keys()}")
print(f"Get login values: {login_info.values()}")
print(f"Get login items: {login_info.items()}") #Key pair is given in tuple

#Popitem() removes last item
last_item = login_info.popitem()
print(f"Removed interest item: {last_item}")

#Update: It inserts new key-value pairs into the dictionary if the keys do not already exist.
#Update: It updates the values of existing keys if they are present in the dictionary.
login_info.update({"customer_age" : 30.5, "profession": "Data Science Professional"})
print(f"Login info after update: {login_info}")

#Get: If we want to fetch any value based on the key, we can have dict['key'] to get the value if the key:value pair is present. But if the 
#key is not present then the code will crash. Hence in order to fetch a value from a dictionary safely, use Get and also mention in the argument
#what to return as a default value if the key is not present.

print(f"Customer's birth place: {login_info.get('customer_birth_place')}")
print(f"Customer's comments: {login_info.get('customer_comments', 'No Comments')}")
print(f"Customer's birth place: {login_info['customer_birth_place']}")
print(f"Customer's comments: {login_info['customer_comments']}")