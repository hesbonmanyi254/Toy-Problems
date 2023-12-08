def two_positive_numbers(a, b, c):
    # Initialize a counter to keep track of positive numbers
    positive_count = 0
    
    # Check if each number is positive and increment the counter
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    # Return True if exactly two numbers are positive, otherwise return False
    return positive_count == 2

# Examples
example1 = (2, 4, -3)
example2 = (-4, 6, 8)
example3 = (4, -6, 9)
example4 = (-4, 6, 0)
example5 = (4, 6, 10)
example6 = (-14, -3, -4)

# Calculate and print results for each example
print(f"For {example1}, the result is: {two_positive_numbers(*example1)}")  # Output: True
print(f"For {example2}, the result is: {two_positive_numbers(*example2)}")  # Output: True
print(f"For {example3}, the result is: {two_positive_numbers(*example3)}")  # Output: True
print(f"For {example4}, the result is: {two_positive_numbers(*example4)}")  # Output: False
print(f"For {example5}, the result is: {two_positive_numbers(*example5)}")  # Output: False
print(f"For {example6}, the result is: {two_positive_numbers(*example6)}")  # Output: False
