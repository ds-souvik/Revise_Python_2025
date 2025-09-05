"""Learn the use of the concepts and keywords nonlocal and global

Global is a reference to global object from anywhere
If you want to reference the variable just in the above function, use nonlocal

Ideally it is not recommended to use the global keyword. Why?
It is quite possible that if multiple people are using the same code base and they have dependencies on the global variable, you might break their code."""

#Idea 1: Vanilla variable values inside and outside the functions after value update
print("Idea 1: Vanilla variable values inside and outside the functions after value update")

item = "sofa"

def update_order():
    item = "table"

    def update_again():
        item ="book-shelf"
        return item
    print(f"Tell me the value of item inside the 2nd function: {update_again().capitalize()}")
    return item

print(f"Tell me the value of item inside the 1st function: {update_order().capitalize()}")
print(f"Tell me the value of item outside all the functions: {item.capitalize()}\n")


#Idea 2: Use nonlocal to change the variable of the 1st function inside 2nd function and it will be valid inside both 1st and 2nd variable.
print("Idea 2: Use nonlocal to change the variable of the 1st function inside 2nd function and it will be valid inside both 1st and 2nd variable.")

item = "sofa"

def update_order():
    item = "table"

    def update_again():
        nonlocal item
        item = "book-shelf"
        return item
    print(f"Tell me the value of item inside the 2nd function: {update_again().capitalize()}")
    return item

print(f"Tell me the value of item inside the 1st function: {update_order().capitalize()}")
print(f"Tell me the value of item outside all the functions: {item.capitalize()}\n")


#Idea 3: Use global to change the global variable inside 2nd function, override the global variable inside 1st variable to see if that remains the same and check the changes in the variable.
print("""Idea 3: Use global to change the global variable inside 2nd function, override the global variable inside 1st variable to see if that remains the same and check the changes in the variable.""")

item = "sofa"

def update_order():
    item = "table"

    def update_again():
        global item
        item = "book-shelf"
        return item
    print(f"Tell me the value of item inside the 2nd function: {update_again().capitalize()}")
    return item

print(f"Tell me the value of item inside the 1st function: {update_order().capitalize()}")
print(f"Tell me the value of item outside all the functions: {item.capitalize()}\n")
