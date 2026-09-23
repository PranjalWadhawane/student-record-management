import json
import os

# File used to store student records
DATA_FILE = "records.json"


def load_records():
    """Load student records from the JSON file."""
    try:
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r") as file:
            records = json.load(file)

        if isinstance(records, list):
            return records

        print("Error: Invalid data format in the file.")
        return []

    except json.JSONDecodeError:
        print("Error: The records file contains invalid JSON data.")
        return []

    except OSError as error:
        print(f"Error reading records file: {error}")
        return []


def save_records(records):
    """Save student records to the JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)

    except OSError as error:
        print(f"Error saving records: {error}")


def get_student_id(records):
    """Generate a new unique student ID."""
    if not records:
        return 1

    return max(student["id"] for student in records) + 1


def add_record(records):
    """Add a new student record."""
    print("\n--- Add Student Record ---")

    try:
        name = input("Enter student name: ").strip()

        if not name:
            raise ValueError("Student name cannot be empty.")

        age = int(input("Enter student age: "))

        if age <= 0:
            raise ValueError("Age must be greater than zero.")

        course = input("Enter course: ").strip()

        if not course:
            raise ValueError("Course cannot be empty.")

        email = input("Enter email: ").strip()

        if not email:
            raise ValueError("Email cannot be empty.")

        student = {
            "id": get_student_id(records),
            "name": name,
            "age": age,
            "course": course,
            "email": email
        }

        records.append(student)
        save_records(records)

        print("Student record added successfully.")

    except ValueError as error:
        print(f"Invalid input: {error}")


def view_records(records):
    """Display all student records."""
    print("\n--- Student Records ---")

    if not records:
        print("No student records found.")
        return

    for student in records:
        print("-" * 40)
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print(f"Email  : {student['email']}")

    print("-" * 40)


def search_records(records):
    """Search for students by ID or name."""
    print("\n--- Search Student Record ---")

    if not records:
        print("No records available for searching.")
        return

    search_value = input("Enter student ID or name: ").strip()

    if not search_value:
        print("Search value cannot be empty.")
        return

    found_records = []

    try:
        student_id = int(search_value)

        for student in records:
            if student["id"] == student_id:
                found_records.append(student)

    except ValueError:
        search_value = search_value.lower()

        for student in records:
            if search_value in student["name"].lower():
                found_records.append(student)

    if found_records:
        print("\nSearch results:")

        for student in found_records:
            print("-" * 40)
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print(f"Email  : {student['email']}")

        print("-" * 40)

    else:
        print("No matching student record found.")


def find_student(records, student_id):
    """Find a student using their ID."""
    for student in records:
        if student["id"] == student_id:
            return student

    return None


def update_record(records):
    """Update an existing student record."""
    print("\n--- Update Student Record ---")

    if not records:
        print("No records available for updating.")
        return

    try:
        student_id = int(input("Enter student ID to update: "))

        student = find_student(records, student_id)

        if student is None:
            print("Student record not found.")
            return

        print("Press Enter to keep the existing value.")

        name = input(f"Name [{student['name']}]: ").strip()

        if name:
            student["name"] = name

        age_input = input(f"Age [{student['age']}]: ").strip()

        if age_input:
            age = int(age_input)

            if age <= 0:
                raise ValueError("Age must be greater than zero.")

            student["age"] = age

        course = input(f"Course [{student['course']}]: ").strip()

        if course:
            student["course"] = course

        email = input(f"Email [{student['email']}]: ").strip()

        if email:
            student["email"] = email

        save_records(records)

        print("Student record updated successfully.")

    except ValueError as error:
        print(f"Invalid input: {error}")


def delete_record(records):
    """Delete a student record using the student ID."""
    print("\n--- Delete Student Record ---")

    if not records:
        print("No records available for deletion.")
        return

    try:
        student_id = int(input("Enter student ID to delete: "))

        student = find_student(records, student_id)

        if student is None:
            print("Student record not found.")
            return

        print(f"Student found: {student['name']}")

        confirmation = input(
            "Are you sure you want to delete it? (y/n): "
        ).lower()

        if confirmation == "y":
            records.remove(student)
            save_records(records)
            print("Student record deleted successfully.")
        else:
            print("Delete operation cancelled.")

    except ValueError:
        print("Invalid ID. Please enter a numeric student ID.")


def display_menu():
    """Display the main application menu."""
    print("\n" + "=" * 45)
    print("       STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student Record")
    print("2. View All Records")
    print("3. Search Student Record")
    print("4. Update Student Record")
    print("5. Delete Student Record")
    print("6. Exit")
    print("=" * 45)


def main():
    """Main function that controls the application."""
    records = load_records()

    print("\nWelcome to the Student Record Management System!")

    while True:
        display_menu()

        try:
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                add_record(records)

            elif choice == "2":
                view_records(records)

            elif choice == "3":
                search_records(records)

            elif choice == "4":
                update_record(records)

            elif choice == "5":
                delete_record(records)

            elif choice == "6":
                print("\nThank you for using the application.")
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 6.")

        except KeyboardInterrupt:
            print("\n\nApplication interrupted by user.")
            break

        except Exception as error:
            print(f"An unexpected error occurred: {error}")


# Start the program
if __name__ == "__main__":
    main()
