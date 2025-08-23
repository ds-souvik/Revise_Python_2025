"""Task Completion Tracker
Instructions: You’re building a simple task tracker for a to-do app. Whenever a user completes tasks, your app should mark them as done.

Tasks: 
    1. Define a function mark_completed_tasks that accepts a list of task names. 
    2. Iterate through the list using a for loop, and update the format like "Completed:  {task}". 
    3. Return a new list with the updated task strings.
"""

# This function will be tested automatically. 
# Do not change the function name or parameters.
def mark_completed_tasks(tasks: list[str]) -> list[str]:
    # Write your code below this line
    complete_status = []
    for task in tasks:
        complete_status.append(f"Completed: {task}")
    
    return complete_status