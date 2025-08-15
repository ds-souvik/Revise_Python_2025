"""We're learning operator overloading here"""

existing_furniture = ["sofa", "table", "tv", "dining table", "fridge", "washing machine", "bed", "study table", "study chair"]

additional_furniture = ['table lamp', 'chandelier', 'wooden paintings']

#Use + to combine 2 lists
new_furniture = existing_furniture + additional_furniture 

print(f"Combine 2 lists other than extend: {new_furniture}")

# * sign means double the items in list in the same order
new_furniture_more_add = existing_furniture + (additional_furniture * 2)

print(f"Get 2 batches of additional furniture for 2 different rooms: {new_furniture_more_add}")


# Bytearray: I didn't understand much operations of bytearray. We'll look into it later
new_item = bytearray("carpet", "utf-8")
print(f"{new_item}")

#an operation example in bytearray
new_item = new_item.replace(b"car", b"bus")
print(f"{new_item}")