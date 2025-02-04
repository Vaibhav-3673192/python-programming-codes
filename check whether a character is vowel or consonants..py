def check_character(char):
    # Convert character to lowercase for case-insensitivity
    char = char.lower()

    # Check if the character is a vowel
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    # Check if the character is a consonant
    elif char.isalpha():
        print(f"{char} is a consonant.")
    else:
        print("Please enter a valid alphabet character.")

# Get user input
char = input("Enter a character: ")

# Check the character
check_character(char)
