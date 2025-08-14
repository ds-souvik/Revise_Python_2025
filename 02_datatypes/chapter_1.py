'''Checking the mutability property of integer'''
sugar_amount = 2 

print(f"Initial sugar amount: {sugar_amount}")

print(f"Initial sugar amount id: {id(sugar_amount)}")

sugar_amount = 12 
print(f"New sugar amount: {sugar_amount}")

print(f"New sugar amount id: {id(sugar_amount)}")

'''Checking the mutability property of set'''

print("***** CHANGE DATATYPE: SET ******")

spice_mix = set() 

print(f"Initial spice mix : {spice_mix}")

print(f"Initial spice mix id: {id(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("cardamom")
print(f"New spice mix : {spice_mix}")

print(f"New spice mix id: {id(spice_mix)}")

