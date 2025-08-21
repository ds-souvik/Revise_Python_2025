"""Numbered Task List
You’re improving the UX of a task management app by numbering the user’s task list automatically.
Tasks: 
    1. Define a function generate_numbered_tasks that takes a list of task names. 
    2. Use the enumerate() function to loop through the list with numbering starting from 1. 
    3. Format each task as "1. Task Name" and return the final list.
"""

# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
	# Write your code below this line
    new_list = []
    for number, task in enumerate(tasks,start=1):
        new_list.append(f"{number}. {task}")
    return new_list