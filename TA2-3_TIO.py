def save_student_info():
    # Accept user input
    last_name = input("Enter Last Name: ")
    first_name = input("Enter First Name: ")
    age = input("Enter Age: ")
    contact_number = input("Enter Contact Number: ")
    course = input("Enter Course: ")
    
    # Format the collected information
    student_info = f"Last Name: {last_name}\nFirst Name: {first_name}\nAge: {age}\nContact Number: {contact_number}\nCourse: {course}\n{'-'*40}\n"
    
    # Open file in append mode and write the information
    with open("students.txt", "a") as file:
        file.write(student_info)
    
    # Display confirmation message
    print("Student information has been save to" + " " + "students.txt")

# Run the function
save_student_info()