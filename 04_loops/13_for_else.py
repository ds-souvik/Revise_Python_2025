"""Learn the usage of for else:
The "for else" construct in Python allows an else block to be associated with a for loop. 
This else block executes only if the for loop completes all of its iterations without 
encountering a break statement."""

staff_name = input("Please share the staff names: ").split(",")
staff_age = input("Please share the staff age: ").split(",")

#[("Souvik", 17), ("Sayli", 14), ("Vedika", 11)]

staff = list(zip(staff_name, staff_age))
print(staff)
for name, age in staff:
    if int(age) > 18:
        print(f"{name} is eligible to manage the staff")
        break

else:
    print(f"No one is eligible to manage the staff")