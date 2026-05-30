# A company wants to track the total bonus paid to all employees and calculate the final salary after performance bonuses.

# Your Tasks
# Global Bonus Tracker

# Create a global variable total_bonus_paid that stores the total bonus paid to all employees.

# Create Function

# Define a function:

# calculate_salary(base_salary: int, performance_score: int) -> int
# Local Variable

# Inside the function, create a local variable final_salary and initialize it with base_salary.

# Nested Bonus Logic

# Define a nested function apply_performance_bonus() inside calculate_salary.

# If performance_score >= 90, add ₹10,000 to final_salary.
# If performance_score >= 75, add ₹5,000 to final_salary.
# Otherwise, no bonus is added.
# Use the nonlocal keyword to modify final_salary.
# Update Global Variable

# After applying the bonus:

# Use the global keyword to update total_bonus_paid.
# Add only the bonus amount (not the entire salary) to total_bonus_paid.
# Return Value

# Return the employee's final salary.

total_bonus_paid = 0 

def calculate_salary(base_salary, performance_score):
    final_salary = base_salary
    
    def apply_performance_bonus():
        nonlocal final_salary
        global total_bonus_paid
        
        if performance_score >= 90 :
            final_salary += 10000
            total_bonus_paid += 10000
        elif performance_score >= 75:
            final_salary += 5000
            total_bonus_paid += 5000
        else : 
            final_salary = final_salary
            total_bonus_paid += 0
        
    apply_performance_bonus()
    return final_salary

salary = calculate_salary(50000, 98)
print(f"Final Salary : {salary}")
print(f"Total Bonus paid : {total_bonus_paid}")