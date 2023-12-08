## Author : HESBON ANGWENYI
## Title  : Toy-Problems

# Python Coding Challenges
This repository contains Python solutions for three coding challenges. Each challenge focuses on different aspects of Python programming. Follow the instructions below to understand the challenges and run the provided solutions.

## Challenges

### Challenge 1: Converting 12-hour time to 24-hour time
Given a 12-hour time, convert it to a 24-hour format.


#### Usage
python
# Example usage
result = convert_to_24_hour(14, 30, "am")  # Should return "1430"
result2 = convert_to_24_hour(8, 10, "am")  # Should return "0810"
result3 = convert_to_24_hour(10, 45, "pm")  # Should return "2245"

# Print the results
print(result)
print(result2)
print(result3)



###  Challenge 2: Two numbers are positive
## usage 
python
# Examples
example1 = (2, 4, -3)
example2 = (-4, 6, 8)
example3 = (4, -6, 9)
example4 = (-4, 6, 0)
example5 = (4, 6, 10)
example6 = (-14, -3, -4)

# Calculate and print results for each example
print(f"For {example1}, the result is: {two_positive_numbers(*example1)}")  # Output: True



###  Challenge 3: Consonant value
## usage
python
# Examples
word1 = "zodiacs"
word2 = "strength"
word3 = "hello"

# Calculate and print consonant values for each example
print(f"The consonant value for '{word1}' is: {solve(word1)}")  # Output: 26
print(f"The consonant value for '{word2}' is: {solve(word2)}")  # Output: 57
print(f"The consonant value for '{word3}' is: {solve(word3)}")  # Output: 0 (no consonants)



## How to Run
1. Ensure you have python installed on your machine
2. Clone this repository
3. Navigate to the project directory
4. Run the Python scripts as needed


## Contributing
Feel free to contribute by adding new challenges, improving existing solutions, or suggesting better ways to approach the problems. 


## MIT License
Copyright (c) 2023 hesbonmanyi254

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
