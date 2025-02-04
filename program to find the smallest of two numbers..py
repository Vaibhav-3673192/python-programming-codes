def find_smallest(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Find and print the smallest number
smallest = find_smallest(num1, num2)
print(f"The smallest number is: {smallest}")
