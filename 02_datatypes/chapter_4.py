'''Operations with tuples'''

furniture = ("sofa", "table", "tv", "dining table", "fridge", "washing machine", "bed", "study table", "study chair")
#This tuple is fixed now. This cannot be changed ever.

#Unpack the components of tuples in a variable. This is a unique syntax
(furniture_1, furniture_2, furniture_3, furniture_4, furniture_5, furniture_6, furniture_7, furniture_8, furniture_9) = furniture

print(f"The most costliest furtniture: {furniture_7}")

print(f"The most costliest furtniture: {furniture[6]}")

print("\n")
#Variable swapping in python doesn't need a 3rd variable
#Making tea for 2 different people with different preferences
milk, water = 3, 4
print(f"Souvik like tea when ratio of milk : water is {milk} : {water}")

milk, water = water, milk
print(f"Sayli like tea when ratio of milk : water is {milk} : {water}")

print('\n')
#check membership/ presence
print(f"Is bed present in furniture list? : {'bed' in furniture}")

print(f"Is Book cupboard present in furniture list? : {'Book cupboard' in furniture}") 

print(f"Is bed present in furniture list? : {'Bed' in furniture}")