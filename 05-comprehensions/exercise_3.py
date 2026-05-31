employees = [
    {"name": "Rahul", "department": "IT", "salary": 65000},
    {"name": "Priya", "department": "HR", "salary": 45000},
    {"name": "Amit", "department": "IT", "salary": 72000},
    {"name": "Neha", "department": "Finance", "salary": 58000},
    {"name": "Vikram", "department": "HR", "salary": 49000}
]

# 1. List Comprehension
# Create a list of employee names whose salary is greater than ₹50,000.
salary_greater_50000 = [employee["name"] for  employee in employees if employee["salary"] > 50000]
print(f"Employees with salary greater that 50000 : {salary_greater_50000}")



# 2. Set Comprehension
# Create a set of all unique departments.
unique_departments = {employee['department'] for employee in employees}
print(f"Unique departments : {unique_departments}")



# 3. Dictionary Comprehension
# Create a dictionary mapping employee names to their departments.
employees_departments = {employee["name"] : employee["department"] for employee in employees}
print(f"Employees to Department : {employees_departments}")



# 4. Generator Expression
# Generate a 10% salary hike for every employee and convert it to a list.

salary = list(employee["salary"]  + employee["salary"] * 0.1  for employee in employees)
print(salary)