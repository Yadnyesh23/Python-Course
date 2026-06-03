# Student Report Card Management System
import json

class StudentExistError(Exception):
    pass

class StudentDoesNotExistError(Exception):
    pass

class SubjectDoesNotExistError(Exception):
    pass

class InvalidMarksError(Exception):
    pass

class Student:
    
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        
    def get_average(self):    
        average = sum(self.marks.values()) / len(self.marks)
        return average
            
    
    def get_grade(self):
        average = self.get_average()
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 45:
            return "D"
        else:
            return "Fail"
    
    def display_details(self):
        return f"Name : {self.name} \nRoll no. : {self.rollno} \nMarks : {self.marks} \nAverage Marks : {self.get_average()} \nGrade : {self.get_grade()}"
    
    

class StudentManager:
    
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        for existing_student in self.students:
            if existing_student.rollno == student.rollno:
                raise StudentExistError("Student already Exists!!")
        self.students.append(student)
        print("Student added succesfully")
    
    def display_students(self):
        students_list = []
        for student in self.students:
            print(student.display_details())
    
    def search_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno :
                return student.display_details()
        raise StudentDoesNotExistError("Students Does not exists!!")
    
    def remove_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                self.students.remove(student)
                print(f'Student with roll number {student.rollno} removed succesfully.')
                return
        raise StudentDoesNotExistError("Student Does not exist")

    def update_marks(self, rollno, subject, marks):

        if not (0 <= marks <= 100):
            raise InvalidMarksError(
                "Marks should be between 0 and 100."
            )

        for student in self.students:

            if student.rollno == rollno:

                if subject not in student.marks:
                    raise SubjectDoesNotExistError(
                        "Subject does not exist."
                    )

                student.marks[subject] = marks

                print(
                    f"{subject} marks updated to {marks} for roll number {rollno}."
                )
                return

        raise StudentDoesNotExistError(
            "Student does not exist."
        )
    
    def get_topper(self):
        topper = self.students[0]
        
        for student in self.students:
            if student.get_average() > topper.get_average():
                topper = student 
        return topper
    
    def save_data(self):
        students_data = []
        
        for student in self.students:
            students_data.append(
                {
                    "name": student.name,
                    "rollno": student.rollno,
                    "marks": student.marks
                }
            )
        
        with open("student_report_card.json", "w") as file:
            json.dump(students_data, file, indent=4)
        
        print("Data saved succesfully!")
    
    def load_data(self):
        with open("student_report_card.json", "r") as file:
            students_data = json.load(file)

        self.students = []

        for student in students_data:

            new_student = Student(
                student["name"],
                student["rollno"],
                student["marks"]
        )

        self.students.append(new_student)
                
                    
        
manager = StudentManager()

student1 = Student("Yash", 56, {
    "Maths": 95,
    "Physics": 90,
    "Chemistry": 91
})

student2 = Student("Aarav", 57, {
    "Maths": 88,
    "Physics": 92,
    "Chemistry": 85
})

student3 = Student("Sneha", 58, {
    "Maths": 97,
    "Physics": 95,
    "Chemistry": 96
})



manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)


print("\nAll Students")
manager.display_students()

manager.save_data()

print("\nSearching Student")
print(manager.search_student(57))

print("\nUpdating Marks")
manager.update_marks(57, "Maths", 100)

print("\nTopper")
print(manager.get_topper().display_details())

print("\nRemoving Student")
manager.remove_student(56)

print("\nRemaining Students")
manager.display_students()

manager.save_data()