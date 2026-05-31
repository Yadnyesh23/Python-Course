students = [
    {"name": "Aman", "marks": 85, "city": "Mumbai"},
    {"name": "Riya", "marks": 92, "city": "Pune"},
    {"name": "Karan", "marks": 78, "city": "Mumbai"},
    {"name": "Sneha", "marks": 92, "city": "Nashik"},
    {"name": "Arjun", "marks": 67, "city": "Pune"}
]

# 1. List Comprehension
# Create a list containing the names of students who scored 80 or more marks.

marks_greater_80 = [student["name"] for student in students if student["marks"] >=80]
print(f"Students with marks 80 or more  : {marks_greater_80}")



# 2. Set Comprehension
# Create a set of all unique cities.

unique_cities = {student['city'] for student in students}
print(f"unique Cities : {unique_cities}")



# 3. Dictionary Comprehension
# Create a dictionary mapping student names to their marks.

students_marks = {student["name"] : student["marks"] for student in students}
print(students_marks)



# 4. Generator Expression
# Generate the squares of all student marks and convert the generator to a list.

squared_marks = list(student["marks"]** 2 for student in students)
print(f"Squared marks : {squared_marks}")

# Using a dictionary comprehension, create a dictionary containing only students who scored above 80:

more_than_80 = {student["name"] : student["marks"] for student in students if student["marks"] > 80}
print(more_than_80)