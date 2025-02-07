def count_characters(input_string):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    num_spaces = 0
    num_others = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
        elif char.isspace():
            num_spaces += 1
        else:
            num_others += 1

    print(f"Vowels: {num_vowels}")
    print(f"Consonants: {num_consonants}")
    print(f"Spaces: {num_spaces}")
    print(f"Other characters: {num_others}")

input_string = "My name is Cristine Joy P. Tio and I am 20 years old."
count_characters(input_string)