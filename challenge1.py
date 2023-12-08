def convert_to_24_hour(hour, minute, period):
    # Check if it's in the afternoon ("pm") and not noon
    if period == "pm" and hour != 12:
        # Convert the hour to 24-hour format by adding 12
        hour += 12
    # Check if it's midnight ("am")
    elif period == "am" and hour == 12:
        # Convert midnight (12:00 am) to 24-hour format (0:00)
        hour = 0

    # Return the formatted time as a string (HHMM)
    return f"{hour:02d}{minute:02d}"

# Example usage with comments
example1 = (10, 30, "am")
example2 = (8, 10, "am")
example3 = (10, 45, "pm")

# Calculate and print results for each example
print(f"For {example1}, the result is: {convert_to_24_hour(*example1)}")  # Should return "1430"
print(f"For {example2}, the result is: {convert_to_24_hour(*example2)}")  # Should return "0810"
print(f"For {example3}, the result is: {convert_to_24_hour(*example3)}")  # Should return "2245"

