
import json

FILENAME = "students.json"


def load_students():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Student file contains invalid data.")
        return []


def save_students(students):
    try:
        with open(FILENAME, "w") as file:
            json.dump(students, file, indent=4)
        print("Records saved successfully.")
    except OSError:
        print("Error: Could not save records.")


def add_student(students):
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter student name: ").strip()

    try:
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))

        if age <= 0 or not 0 <= marks <= 100:
            print("Age must be positive and marks must be from 0 to 100.")
            return

    except ValueError:
        print("Invalid input. Age must be an integer and marks a number.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")


def show_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student found:", student)
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n--- Student Record Manager ---")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()