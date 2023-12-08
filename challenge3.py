def solve(word):
    # Define a string containing vowels
    vowels = "aeiou"

    # Create a list comprehension to calculate the values of consonants
    # Convert each character to lowercase to make the comparison case-insensitive
    consonant_values = [ord(char) - ord("a") + 1 for char in word.lower() if char not in vowels]

    # Check if there are no consonants in the word
    if not consonant_values:
        return 0

    # Return the maximum value among the consonant values
    return max(consonant_values)

# Examples
word1 = "zodiacs"
word2 = "strength"
word3 = "hello"

# Calculate and print consonant values for each example
print(f"The consonant value for '{word1}' is: {solve(word1)}")  # Output: 26
print(f"The consonant value for '{word2}' is: {solve(word2)}")  # Output: 57
print(f"The consonant value for '{word3}' is: {solve(word3)}")  # Output: 0 (no consonants)
