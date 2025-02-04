def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is negative
if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    # Call the factorial function and display the result
    print(f"The factorial of {number} is {factorial(number)}.")
