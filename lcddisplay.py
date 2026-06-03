# ==========================================================
# Experiment No. 3
# Title: LCD Display
# Aim:
# To display numbers in a seven-segment LCD style
# similar to a calculator display.
# ==========================================================

# Seven-segment patterns for digits 0-9
lcd = {
    '0': [" - ",
          "| |",
          "   ",
          "| |",
          " - "],

    '1': ["   ",
          "  |",
          "   ",
          "  |",
          "   "],

    '2': [" - ",
          "  |",
          " - ",
          "|  ",
          " - "],

    '3': [" - ",
          "  |",
          " - ",
          "  |",
          " - "],

    '4': ["   ",
          "| |",
          " - ",
          "  |",
          "   "],

    '5': [" - ",
          "|  ",
          " - ",
          "  |",
          " - "],

    '6': [" - ",
          "|  ",
          " - ",
          "| |",
          " - "],

    '7': [" - ",
          "  |",
          "   ",
          "  |",
          "   "],

    '8': [" - ",
          "| |",
          " - ",
          "| |",
          " - "],

    '9': [" - ",
          "| |",
          " - ",
          "  |",
          " - "]
}

# Input number
number = input("Enter a number: ")

print("\nLCD Display:\n")

# Print row by row
for row in range(5):

    for digit in number:
        print(lcd[digit][row], end=" ")

    print()


# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter a number: 21
#
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# LCD Display:
#
#  -      
#   |   |
#  -     
# |     |
#  -     
#
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Create a dictionary containing LCD patterns
#    for digits 0 to 9.
# 2. Read a number from the user.
# 3. Each digit is represented using 5 rows.
# 4. Print the digits row by row.
# 5. Combine patterns to display the complete number.
#
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Store LCD patterns for digits 0-9
# Step 3: Input a number
# Step 4: For each row (0 to 4)
#             Print corresponding row of each digit
# Step 5: Move to next line
# Step 6: Display complete LCD number
# Step 7: Stop
#
#
# ==========================================================
# RESULT
# ==========================================================
#
# The given number was successfully displayed
# in seven-segment LCD format.
#
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. What is a seven-segment display?
# Ans:
# A seven-segment display is an electronic display
# device used to show digits using seven segments.
#
#
# Q2. How many segments are there in one digit?
# Ans:
# There are 7 segments:
# Top, Middle, Bottom,
# Top-Left, Top-Right,
# Bottom-Left, Bottom-Right.
#
#
# Q3. How do you map each digit to its segments?
# Ans:
# Using a dictionary where each digit stores
# its LCD pattern.
#
#
# Q4. How can you modify the program to scale
# the digit size?
# Ans:
# By increasing the number of spaces and
# repeating horizontal and vertical segments.
#
#
# Q5. What characters are typically used for
# horizontal and vertical segments?
# Ans:
# Horizontal segments use '-'
# Vertical segments use '|'
#
#
# ==========================================================
# SHORT VIVA ANSWERS (EXAM READY)
# ==========================================================
#
# 1. What is LCD Display?
#    A seven-segment display used to show digits.
#
# 2. How many segments are used?
#    Seven segments.
#
# 3. Which data structure is used?
#    Dictionary.
#
# 4. Why use pattern mapping?
#    To store and display digit shapes easily.
#
# 5. Time Complexity?
#    O(n), where n is the number of digits.
#
# ==========================================================