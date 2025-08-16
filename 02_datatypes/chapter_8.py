'''Operations with set'''

essential_furniture = {"sofa", "bed", "cupboard", "fridge", "washing machine"}

optional_furniture = {"Tv", "Table", "washing machine"}

#Union of 2 sets: |
all_furniture = essential_furniture | optional_furniture
print(f"Union of all furniture: {all_furniture}")

#Common between 2 sets: &
common_furniture = essential_furniture & optional_furniture
print(f"Common in essential and optional furniture: {common_furniture}")

#Difference of 2 sets A-B: give me items only in A by removing the common item from B: -
difference = essential_furniture - optional_furniture
print(f"Only essential furniture and not common with optional: {difference}")

#Membership test: in
print(f"Is 'washing machine' in essential_firniture? \n{'washing machine' in essential_furniture}")