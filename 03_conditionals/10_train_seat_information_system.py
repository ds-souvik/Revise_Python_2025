"""Build a Train seat information system
You're building a ticket info system for a railway app.
Based on seat type, show its features.

Task:
    1. Input: 'sleeper', 'AC', 'general', 'luxury'
    2. Match using match-case.
    3. Unknown -> show 'Invalid seat type' """

def train_seat_info(coach_type):
    match coach_type:
        case "sleeper":
            return "Comfortable seat but no AC"
        case "ac":
            return "Comfortable seat with AC" 
        case "luxury":
            return "Comfortable seat, AC, food and housekeeping"
        case "general":
            return "Congested, crowded and uncomfortable journey"
        case _:
            return "Invalid seat type. Please try again"

user_name = input("Please tell us your name: ")

coach_info = input(f"Hello {user_name}, please let us know your coach type: ").lower()

print(train_seat_info(coach_info))