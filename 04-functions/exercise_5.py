# Student Report Generator

# You are building a system that generates a report card for students.

# Function
# generate_report(student_name="Unknown", *marks, **details)
# Parameters
# student_name: Defaults to "Unknown" if not provided.
# *marks: Any number of integer marks.
# **details: Additional information such as:
# course="AI & DS"
# year=2
# city="Mumbai"
# Report Format
# Header
# Student Report
# Student Information
# Name: Yadnyesh
# Details Section

# Only display if details are provided.

# Details:
# Course: AI & DS
# Year: 2
# City: Mumbai
# Marks Section

# Only display if marks are provided.

# Marks:
# - 85
# - 90
# - 78
# Summary

# Calculate:

# Total Marks
# Average Marks

# Display:

# Total: 253
# Average: 84.33
# Grade Logic
# Average ≥ 90 → A
# Average ≥ 75 → B
# Average ≥ 60 → C
# Otherwise → D

# Display:

# Grade: B

def generate_report(student_name, *marks, **details):
    lines=[]
    
    lines.append("Student Report")
    
    lines.append(f"Name : {student_name}")
    
    if details:
        lines.append("Details:")
        for key, value in details.items():
            lines.append(f"{key.capitalize()} : {value}")
            
    if marks:
        lines.append("Marks : ")
        for mark in marks:
            lines.append(f"- {mark}")
        
    total_marks = sum(marks)
    avg_marks = total_marks / len(marks)
    
    lines.append(f"Total marks : {total_marks}")
    lines.append(f"Average marks : {avg_marks}")
    
    if avg_marks>= 90:
        lines.append("Grade : A")
    elif avg_marks >= 75 :
        lines.append('Grade : B')
    elif avg_marks >= 60 :
        lines.append('Grade : C')
        
    return "\n".join(lines)

report = generate_report("Yadnyesh", 85, 90, 67, 75, course="AI-DS", year=2)
print(report)