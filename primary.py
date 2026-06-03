# ==========================================================
# Experiment No. 21
# Title: Primary Arithmetic
# Aim:
# To count the number of carry operations that occur
# while adding two multi-digit numbers.
# ==========================================================

# Take two numbers from user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Reverse numbers to process from right to left
num1 = num1[::-1]
num2 = num2[::-1]

carry = 0
carry_count = 0

# Find maximum length
max_len = max(len(num1), len(num2))

# Check each digit position
for i in range(max_len):

    # If digit does not exist, take 0
    digit1 = int(num1[i]) if i < len(num1) else 0
    digit2 = int(num2[i]) if i < len(num2) else 0

    # Add digits and previous carry
    total = digit1 + digit2 + carry

    # Check if carry is generated
    if total >= 10:
        carry_count += 1
        carry = 1
    else:
        carry = 0

# Display result
if carry_count == 0:
    print("No carry operation.")

elif carry_count == 1:
    print("1 carry operation.")

else:
    print(carry_count, "carry operations.")


# ==========================================================
# SAMPLE INPUT 1
# ==========================================================
#
# Enter first number: 123
# Enter second number: 456
#
# ==========================================================
# SAMPLE OUTPUT 1
# ==========================================================
#
# No carry operation.
#
#
# ==========================================================
# SAMPLE INPUT 2
# ==========================================================
#
# Enter first number: 555
# Enter second number: 555
#
# ==========================================================
# SAMPLE OUTPUT 2
# ==========================================================
#
# 3 carry operations.
#
#
# ==========================================================
# SAMPLE INPUT 3
# ==========================================================
#
# Enter first number: 123
# Enter second number: 594
#
# ==========================================================
# SAMPLE OUTPUT 3
# ==========================================================
#
# 1 carry operation.
#
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Read two numbers as strings.
# 2. Reverse both numbers so that processing starts
#    from the rightmost digit.
# 3. Initialize carry = 0 and carry_count = 0.
# 4. Add corresponding digits one by one.
# 5. If sum is greater than or equal to 10,
#    generate a carry.
# 6. Increase carry_count.
# 7. Continue until all digits are processed.
# 8. Display total carry operations.
#
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Input two numbers
# Step 3: Reverse both numbers
# Step 4: Initialize carry = 0
# Step 5: For each digit position
#           Add digits and carry
#           If sum >= 10
#               carry_count += 1
#               carry = 1
#           Else
#               carry = 0
# Step 6: Display carry count
# Step 7: Stop
#
#
# ==========================================================
# RESULT
# ==========================================================
#
# The number of carry operations generated during
# addition was successfully counted.
#
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. What is a carry operation?
# Ans:
# A carry operation occurs when the sum of two digits
# is 10 or more and 1 is carried to the next digit.
#
# Q2. Why do we process digits from right to left?
# Ans:
# Because addition starts from the least significant
# digit (rightmost digit).
#
# Q3. Can this problem be solved without converting
# numbers to strings?
# Ans:
# Yes, by repeatedly using modulus (%) and division (//)
# operations to extract digits.
#
# Q4. What is the time complexity of this approach?
# Ans:
# O(n), where n is the number of digits.
#
# Q5. How does carry propagation affect multi-digit addition?
# Ans:
# A carry generated at one position is added to the next
# higher digit, affecting the final result.
#
# ==========================================================