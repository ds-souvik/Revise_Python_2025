'''Operations with lists'''
furniture = ["sofa", "table", "tv", "dining table", "fridge", "washing machine", "bed", "study table", "study chair"]

#add a new item

furniture.append('book shelf')

print(f"New furniture set: {furniture}")

print('\n')

furniture.remove("table")

print(f"Latest furniture set after selling table: {furniture}")

print('\n')

buy_new_sets = ['table lamp', 'chandelier', 'wooden paintings']

furniture.extend(buy_new_sets)

print(f"New furniture set after buying few items: {furniture}")

print('\n')
#Insert sofa cover right after sofa and bed sheet right after bed

furniture.insert(1, 'sofa cover')
furniture.insert(7, 'bed sheet')

print(f"New set of furniture: {furniture}")

#pop: remove the last word from the list and give it to the variqble
last_added_item = furniture.pop()

print(f"The last added item is: {last_added_item}")
print('\n')
print(f"Current state of furniture list: {furniture}")

print('\n')

furniture.reverse()
print(f"My furniture list in reverse: {furniture}")

print('\n')

furniture.sort()
print(f"Sorting my furniture list: {furniture}")
print('\n')

#Max function in a list
age_of_colleagues = [48, 32, 51, 24, 39]
print(f"The maximum age in our team is: {max(age_of_colleagues)}")
print(f"The minimum age in our team is: {min(age_of_colleagues)}")