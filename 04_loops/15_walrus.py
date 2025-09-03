"""Understood the usage of walrus operator"""

value = 10
remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is :{remainder}")

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")
else:
    print(f"Perfectly divisible")

#It can also be used to take inputs while in if-else structure

school_students = ["Souvik", "Sayli", "Sumita", "Debdas"]

if (name :=input("Mention the name of the student : ").lower()) in [element.lower() for element in school_students]:
    print(f"Student {name.capitalize()} is from our school")
else:
    print(f"Student {name.capitalize()} is not from our school")

#if else using ternary operator and also using walrus operator and comprehensions

school_students = ["Souvik", "Sayli", "Sumita", "Debdas"]

print(f"Student {wal_name.capitalize()} is from our school") if (wal_name := input("Mention the name of the student: ").lower()) in [element.lower() for element in school_students] else print(f"Student {wal_name.capitalize()} not in our school")