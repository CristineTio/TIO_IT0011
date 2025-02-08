def read_student_info():
    
    try:
        with open("students.txt", "r") as file:
            content = file.read()
   
            if not content:
                print("No student information found.")
            else:
                print("\nReading student information:\n")
                print(content)
    except FileNotFoundError:
        print("Error: The file 'students.txt' does not exist.")

read_student_info()