firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

print("Full name: " + firstName + " " + lastName)
print("Full Name (Upper Case): " + firstName.upper() + " " + lastName.upper())
print("Full Name (Lower Case): " + firstName.lower() + " " + lastName.lower())
print("Length of Full Name: " + str(len(firstName) + len(lastName)))