"""HIDING IMLEMENTATION DETAILS.

You're building a simle app that register users.
You want to seperate concerns: getting input, validating it and saving it.

Task: Write register_users() that calls:
    1. get_input()
    2. validate_input()
    3. save to db()"""

data_dict = {"Gujarat": ["Bharuch", "Vadodara", "Surat", "Ahmedabad", "Gandhinagar", "Vapi", "Valsad", "Navsari", "Anand", "Saurashtra", "Kutch"]}

def get_input():
    name = input(f"Name: ")
    email_id = input(f"E-mail id: ")
    phone_num = int(input(f"Contact no: "))
    city = input(f"City: ")
    state = input(f"State: ")
    return name, email_id, phone_num, city, state

def validate_input(name, email_id, phone_num, city, state):
    flag = 0
    if not isinstance(name, str): 
        print("Invalid Name")
        flag +=1

    if not "@" in email_id or not ".com" in email_id:
        print("Invalid Email id")
        flag +=1

    if len(str(phone_num)) != 10 or not isinstance(phone_num, int):
        print("Invalid Phone number")
        flag +=1
    
    if state.lower() not in [st.lower() for st in data_dict.keys()]:
        print("Invalid State")
        flag +=1
    elif city.lower() not in [ct.lower() for ct in data_dict[state.capitalize()]]:
        print("Invalid City")
        flag +=1
    
    return flag

def save_to_db(flag, name, email_id, phone_num, city, state):
    if flag == 0:
        print("Registered successfully")
    else:
        print("Please try again..")

def register_users():
    user_name, user_email_id, user_phone_num, user_city, user_state = get_input()
    validation_flag = validate_input(user_name, user_email_id, user_phone_num, user_city, user_state)
    save_to_db(validation_flag, user_name, user_email_id, user_phone_num, user_city, user_state)

register_users()

    