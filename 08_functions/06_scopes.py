"""Learn and understand scopes:

Concept 1: Difference between local and global scope
Concept 2: Enclosing scope
Concept 3: Overriding enclosing scope
Concept 4: Cannot call an inner function of a nested function outside
"""

print("Concept 1: Difference between local and global scope \n")
def serve_chai():
    chai_type = "Masala"  #local scope
    return chai_type

chai_type = "Lemon" #global scope
print(f"Returning the function serve_chai() that has a function chai_type : {serve_chai()}\n")
print(f"Printing the outside variable chai_type: {chai_type}")

#------------------------------------------------------------------------------------

'''Nested Function'''
print("Concept 2: Enclosing scope \n")
def outer_chai_counter():
    chai_order = "Lemon"  #enclosing scope

    def inner_chai_order():
        return chai_order

    return inner_chai_order()

print(outer_chai_counter())

#------------------------------------------------------------------------------------

print("Concept 3: Overriding enclosing scope. Only the variable's value has chaged only inside the nested function \n")
def outer_chai_counter():
    chai_order = "Lemon"  #enclosing scope

    def inner_chai_order():
        chai_order = "Ginger"
        return f"Inner chai_order value: {chai_order}"
    print(f"Outer chai_order value: {chai_order}")
    return inner_chai_order()

print(outer_chai_counter())


#------------------------------------------------------------------------------------

print("Concept 4: Cannot call an inner function of a nested function outside\n")
def outer_chai_counter():
    chai_order = "Lemon"  #enclosing scope

    def inner_chai_order():
        chai_order = "Ginger"
        return f"Inner chai_order value: {chai_order}"
    print(f"Outer chai_order value: {chai_order}")
    return inner_chai_order()

print(inner_chai_counter())