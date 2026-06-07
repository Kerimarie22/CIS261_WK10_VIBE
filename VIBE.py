# KERI LOGAB
# CIS261
# WK10 VIBE Coding

import os

class Student:
    def __init__(self, name, student_id, test1, test2, test3):
        self.name = name
        self.id = student_id
        self.test1 = float(test1)
        self.test2 = float(test2)
        self.test3 = float(test3)
        self.average = 0.0
        self.grade = ""
        self.calculate_average_and_grade()

    def calculate_average_and_grade(self):
        self.average = (self.test1 + self.test2 + self.test3) / 3.0
        if self.average >= 90:
            self.grade = "A"
        elif self.average >= 80:
            self.grade = "B"
        elif self.average >= 70:
            self.grade = "C"
        elif self.average >= 60:
            self.grade = "D"
        else:
            self.grade = "F"

    def to_file_line(self):
        return f"{self.name}|{self.id}|{self.test1:.2f}|{self.test2:.2f}|{self.test3:.2f}|{self.average:.2f}|{self.grade}"


def load_records(filename="student_grades.txt"):
    students = []
    if not os.path.exists(filename):
        return students
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) == 7:
                    name, student_id, t1, t2, t3, _, _ = parts
                    student = Student(name, student_id, float(t1), float(t2), float(t3))
                    students.append(student)
    except IOError as e:
        print(f"Error loading file: {e}")
    return students


def save_records(students, filename="student_grades.txt"):
    try:
        with open(filename, "w") as file:
            for student in students:
                file.write(student.to_file_line() + "\n")
        print("Records saved successfully.")
    except IOError as e:
        print(f"Error saving file: {e}")


def get_numeric_input(prompt):
    while True:
        value = input(prompt).strip()
        if value.upper() == "ESC":
            return "ESC"
        try:
            float_val = float(value)
            if 0 <= float_val <= 100:
                return float_val
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")


def add_student(students):
    print("\n--- Add New Student Record ---")
    name = input("Enter student name (or type ESC to return): ").strip()
    if name.upper() == "ESC" or not name:
        return

    student_id = input("Enter student ID (or type ESC to return): ").strip()
    if student_id.upper() == "ESC" or not student_id:
        return

    t1 = get_numeric_input("Enter Test 1 score: ")
    if t1 == "ESC":
        return
    t2 = get_numeric_input("Enter Test 2 score: ")
    if t2 == "ESC":
        return
    t3 = get_numeric_input("Enter Test 3 score: ")
    if t3 == "ESC":
        return

    student = Student(name, student_id, t1, t2, t3)
    students.append(student)
    print(f"Student {name} added successfully.")


def display_all_students(students):
    print("\n--- Student Records ---")
    if not students:
        print("No student records found.")
        return
    print(f"{'Name':<20} | {'ID':<10} | {'Test 1':<8} | {'Test 2':<8} | {'Test 3':<8} | {'Average':<8} | {'Grade':<5}")
    print("-" * 75)
    for s in students:
        print(f"{s.name:<20} | {s.id:<10} | {s.test1:<8.2f} | {s.test2:<8.2f} | {s.test3:<8.2f} | {s.average:<8.2f} | {s.grade:<5}")


def search_student(students):
    print("\n--- Search Student ---")
    if not students:
        print("No student records available to search.")
        return
    search_name = input("Enter student name to search: ").strip().lower()
    if search_name.upper() == "ESC" or not search_name:
        return

    found = False
    for s in students:
        if s.name.lower() == search_name:
            if not found:
                print(f"\n{'Name':<20} | {'ID':<10} | {'Test 1':<8} | {'Test 2':<8} | {'Test 3':<8} | {'Average':<8} | {'Grade':<5}")
                print("-" * 75)
            print(f"{s.name:<20} | {s.id:<10} | {s.test1:<8.2f} | {s.test2:<8.2f} | {s.test3:<8.2f} | {s.average:<8.2f} | {s.grade:<5}")
            found = True
    if not found:
        print("Student not found.")


def display_class_statistics(students):
    print("\n--- Class Statistics ---")
    if not students:
        print("No student records available to calculate statistics.")
        return

    highest = max(s.average for s in students)
    lowest = min(s.average for s in students)
    class_avg = sum(s.average for s in students) / len(students)

    print(f"Highest Average: {highest:.2f}")
    print(f"Lowest Average:  {lowest:.2f}")
    print(f"Class Average:   {class_avg:.2f}")


def main():
    students = load_records()
    while True:
        print("\n=== Student Grade Calculator ===")
        print("1. Add New Student Record")
        print("2. Display All Students")
        print("3. Search for a Student by Name")
        print("4. View Class Statistics")
        print("5. Save and Exit (or type ESC)")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            display_class_statistics(students)
        elif choice == "5" or choice.upper() == "ESC":
            save_records(students)
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
