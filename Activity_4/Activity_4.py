import json
import os

def load_records(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_records(filename, records):
    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)

def calculate_grade(record):
    return (record[2] * 0.6) + (record[3] * 0.4)

def show_records(records):
    for record in records:
        print(record)

def add_record(records):
    student_id = input("Enter Student ID (6 digits): ")
    name = input("Enter Full Name (First Last): ").split()
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    records.append((student_id, tuple(name), class_standing, major_exam))
    print("Record added successfully.")

def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            name = input("Enter New Full Name (First Last): ").split()
            class_standing = float(input("Enter New Class Standing Grade: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            records[i] = (student_id, tuple(name), class_standing, major_exam)
            print("Record updated.")
            return
    print("Student ID not found.")

def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted.")
            return
    print("Student ID not found.")

def show_student(records):
    student_id = input("Enter Student ID: ")
    for record in records:
        if record[0] == student_id:
            print(record)
            return
    print("Student ID not found.")

def main():
    filename = "records.json"
    records = load_records(filename)
    
    while True:
        print("\n1. Show All Records\n2. Order by Last Name\n3. Order by Grade\n4. Show Student Record\n5. Add Record\n6. Edit Record\n7. Delete Record\n8. Save\n9. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            show_records(records)
        elif choice == '2':
            show_records(sorted(records, key=lambda r: r[1][1]))
        elif choice == '3':
            show_records(sorted(records, key=calculate_grade, reverse=True))
        elif choice == '4':
            show_student(records)
        elif choice == '5':
            add_record(records)
        elif choice == '6':
            edit_record(records)
        elif choice == '7':
            delete_record(records)
        elif choice == '8':
            save_records(filename, records)
            print("Records saved.")
        elif choice == '9':
            break
        else:
            print("Invalid choice. Try again.")
    
if __name__ == "__main__":
    main()
