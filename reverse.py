# ==========================================================
# Experiment No. 22
# Title: Reverse and Add
# Aim:
# To generate a palindrome by repeatedly reversing
# a number and adding it to the original number.
# ==========================================================

# Take input number from user
num = int(input("Enter a number: "))

# Count how many reverse-add operations are performed
count = 0

# Repeat until palindrome is found
while True:

    # Reverse the number
    reverse_num = int(str(num)[::-1])

    # Add original number and reversed number
    num = num + reverse_num

    # Increase iteration count
    count += 1

    # Check if result is palindrome
    if str(num) == str(num)[::-1]:
        break

# Display result
print("\nIterations:", count)
print("Palindrome:", num)


# ==========================================================
# SAMPLE INPUT 1
# ==========================================================
#
# Enter a number: 195
#
# ==========================================================
# SAMPLE OUTPUT 1
# ==========================================================
#
# Iterations: 4
# Palindrome: 9339
#
#
# ==========================================================
# SAMPLE INPUT 2
# ==========================================================
#
# Enter a number: 265
#
# ==========================================================
# SAMPLE OUTPUT 2
# ==========================================================
#
# Iterations: 5
# Palindrome: 45254
#
#
# ==========================================================
# SAMPLE INPUT 3
# ==========================================================
#
# Enter a number: 750
#
# ==========================================================
# SAMPLE OUTPUT 3
# ==========================================================
#
# Iterations: 3
# Palindrome: 6666
#
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Read a number from the user.
# 2. Reverse the digits of the number.
# 3. Add the reversed number to the original number.
# 4. Check whether the result is a palindrome.
# 5. If not, repeat the process.
# 6. Count the number of iterations.
# 7. Display the palindrome and iteration count.
#
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Input number n
# Step 3: Set count = 0
# Step 4: Reverse n
# Step 5: Compute n = n + reverse(n)
# Step 6: Increment count
# Step 7: Check if n is palindrome
# Step 8: If not palindrome, repeat Step 4
# Step 9: Print count and palindrome
# Step 10: Stop
#
#
# ==========================================================
# OBSERVATION TABLE
# ==========================================================
#
# Test Case    Input    Iterations    Palindrome
# ------------------------------------------------
# 1            195      4             9339
# 2            265      5             45254
# 3            750      3             6666
#
#
# ==========================================================
# RESULT
# ==========================================================
#
# A palindrome number was successfully generated
# using the Reverse and Add technique.
#
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. What is a palindrome number?
# Ans:
# A palindrome number reads the same from left
# to right and right to left.
#
# Example:
# 121, 1331, 9449
#
#
# Q2. Explain the Reverse and Add process.
# Ans:
# Reverse the digits of a number, add it to the
# original number, and repeat until a palindrome
# is obtained.
#
#
# Q3. Does this method always produce a palindrome?
# Ans:
# For most numbers yes, but for some numbers
# (called Lychrel candidates) a palindrome has
# not been found.
#
#
# Q4. What is a Lychrel number?
# Ans:
# A Lychrel number is a number that does not form
# a palindrome through the reverse-and-add process.
#
#
# Q5. What is the time complexity of this algorithm?
# Ans:
# O(k × d)
#
# where:
# k = number of iterations
# d = number of digits in the number
#
# ==========================================================