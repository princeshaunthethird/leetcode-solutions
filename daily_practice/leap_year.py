
year = int(input("Enter the year"))
"""
Determines whether a given year is a leap year.

A leap year is defined as:
- A year divisible by 400 and divisible by 100 for century years
- A year divisible by 4 but NOT divisible by 100 for normal years

Args:
    year (int): The year to check, provided as user input.

Returns:
    None: Prints the result indicating whether the year is a leap year or not.

Example:
    Enter the year: 2024
    Output: The year 2024 is a leap year
"""

if((year % 400 == 0) and (year % 100 == 0 )):
    print(f"The year {year} is a leap year")
elif((year % 4 == 0 ) and (year % 100 != 0)):
    print(f"the year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")