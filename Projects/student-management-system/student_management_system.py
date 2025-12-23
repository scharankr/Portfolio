# Student Management System
# Author: Charan

students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course Name: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("\n✅ Student added successfully!\n")

def view_students():
    if not students:
        print("\n⚠️ No student records found.\n")
        return

    print("\n📋 Student Records:")
    for student in students:
        print("----------------------------")
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
    print()

def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["course"] = input("Enter new course: ")
            print("\n✅ Student record updated successfully!\n")
            return

    print("\n❌ Student not found.\n")

def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("\n✅ Student record deleted successfully!\n")
            return

    print("\n❌ Student not found.\n")

def main_menu():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("\n👋 Exiting program. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice. Please try again.\n")

# Run the program
main_menu()
