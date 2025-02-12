def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            for idx, line in enumerate(lines, start=1):
                numbers = list(map(int, line.strip().split(',')))
                total = sum(numbers)
                result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
                print(f"Line {idx}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except ValueError:
        print("Error: File contains invalid data.")

# Run the program
process_file("numbers.txt")
