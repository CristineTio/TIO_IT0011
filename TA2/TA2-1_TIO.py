firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

print("Hello, " + firstName + " " + lastName + "!")
print(firstName[0:4])
print("Greeting Message: " + "Hello, " + firstName[0:4] + "!" + " " +"Welcome. You are", age, "years old.")