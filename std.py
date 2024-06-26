class Student:
    def _init_(self, name, reg_no, mark1, mark2, mark3):
        self.name = name
        self.reg_no = reg_no
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

def create_students():
    students = {}
    num_students = int(input("Enter the number of students to be created: "))
    
    for _ in range(num_students):
        name = input("Enter the student's name: ")
        reg_no = input("Enter the student's registration number: ")
        mark1 = float(input("Enter the mark for subject 1: "))
        mark2 = float(input("Enter the mark for subject 2: "))
        mark3 = float(input("Enter the mark for subject 3: "))
        
        student = Student(name, reg_no, mark1, mark2, mark3)
        students[reg_no] = student
    
    return students

def print_students(students):
    for reg_no, student in students.items():
        print(f"Name: {student.name}, Reg No: {reg_no}, Marks: {student.mark1}, {student.mark2}, {student.mark3}")


students = create_students()
print_students(students)
