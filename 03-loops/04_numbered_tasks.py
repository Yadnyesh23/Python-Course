# You’re improving the UX of a task management app
# by numbering the user’s task list automatically.

# Define the task list.
# Use the enumerate() function to loop through the list with numbering starting from 1.
# Format each task as "1. Task Name" and return the final list.

tasks = ['Coding' , 'Study', 'Gym', 'Sleep', 'Walk']

for idx, task in enumerate(tasks, start=1):
    print(f"{idx}. {task}")