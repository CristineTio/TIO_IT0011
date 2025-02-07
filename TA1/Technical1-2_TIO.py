def sum_of_digits(input_string):
    total_sum = 0

    for char in input_string:
        if char.isdigit():
            total_sum += int(char)

    print(f"Sum of digits: {total_sum}")

input_string = "Cristine Tio - 20 years old."
sum_of_digits(input_string)