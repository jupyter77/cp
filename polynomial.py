# ==========================================================
# Experiment No. 23
# Title: Polynomial Coefficients
# Aim:
# To compute the coefficient of a term in the expansion
# of (x1 + x2 + ... + xk)^n using the Multinomial Theorem.
# ==========================================================

# Function to calculate factorial
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact


# Input n and k
n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))

# Input n1, n2, ..., nk
powers = []

print("Enter", k, "values:")

for i in range(k):
    value = int(input(f"n{i+1}: "))
    powers.append(value)

# Verify sum of powers equals n
if sum(powers) != n:
    print("\nError: Sum of n1 + n2 + ... + nk must be equal to n")

else:

    # Calculate denominator
    denominator = 1

    for value in powers:
        denominator *= factorial(value)

    # Multinomial coefficient formula
    coefficient = factorial(n) // denominator

    print("\nCoefficient =", coefficient)


# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter value of n: 5
# Enter value of k: 3
#
# Enter 3 values:
# n1: 2
# n2: 2
# n3: 1
#
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# Coefficient = 30
#
#
# ==========================================================
# CALCULATION
# ==========================================================
#
# n = 5
# k = 3
#
# n1 = 2
# n2 = 2
# n3 = 1
#
# Formula:
#
#            n!
# --------------------------------
#  n1! × n2! × n3! × ... × nk!
#
#
#            5!
# --------------------------------
#       2! × 2! × 1!
#
#
#           120
# --------------------------------
#         2 × 2 × 1
#
#
# = 30
#
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Read values of n and k.
# 2. Read k powers (n1, n2, ..., nk).
# 3. Verify that:
#
#       n1 + n2 + ... + nk = n
#
# 4. Compute factorial of n.
# 5. Compute factorial of each ni.
# 6. Apply multinomial coefficient formula.
# 7. Display the coefficient.
#
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Input n and k
# Step 3: Input n1, n2, ..., nk
# Step 4: Verify sum of all ni equals n
# Step 5: Compute factorial(n)
# Step 6: Compute factorial of each ni
# Step 7: Calculate:
#
#          n!
# -----------------------
# n1! × n2! × ... × nk!
#
# Step 8: Display coefficient
# Step 9: Stop
#
#
# ==========================================================
# RESULT
# ==========================================================
#
# The multinomial coefficient was successfully
# calculated using factorials and the
# Multinomial Theorem.
#
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. What is the Binomial Theorem?
# Ans:
# The Binomial Theorem gives the expansion of
# (a + b)^n using combinations.
#
#
# Q2. What is Factorial?
# Ans:
# Factorial of a number n is:
#
# n! = n × (n-1) × (n-2) × ... × 1
#
# Example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
#
#
# Q3. What is the Multinomial Theorem?
# Ans:
# It is an extension of the Binomial Theorem
# used for expressions having more than
# two variables.
#
#
# Q4. What is a Multinomial Coefficient?
# Ans:
# It represents the coefficient of a term
# in the expansion of:
#
# (x1 + x2 + ... + xk)^n
#
#
# Q5. What is the time complexity of this program?
# Ans:
# O(n + k)
#
# where:
# n = value used for factorial calculation
# k = number of variables.
#
# ==========================================================