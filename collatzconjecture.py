# ==========================================================
# Experiment No. 1
# Title: 3n + 1 Problem (Collatz Conjecture)
# Aim:
# To compute the maximum cycle length for numbers
# between two given integers using the Collatz sequence.
# ==========================================================

# Function to calculate cycle length
def cycle_length(n):

    count = 1

    while n != 1:

        # If number is even
        if n % 2 == 0:
            n = n // 2

        # If number is odd
        else:
            n = 3 * n + 1

        count += 1

    return count


# Input two numbers
i = int(input("Enter first number: "))
j = int(input("Enter second number: "))

# Keep original values for output
original_i = i
original_j = j

# Ensure smaller value comes first
start = min(i, j)
end = max(i, j)

max_cycle = 0

# Check cycle length for every number
for num in range(start, end + 1):

    length = cycle_length(num)

    if length > max_cycle:
        max_cycle = length

# Display result
print("\nOutput:")
print(original_i, original_j, max_cycle)


# ==========================================================
# SAMPLE INPUT 1
# ==========================================================
#
# Enter first number: 1
# Enter second number: 10
#
#
# ==========================================================
# SAMPLE OUTPUT 1
# ==========================================================
#
# Output:
# 1 10 20
#
#
# ==========================================================
# SAMPLE INPUT 2
# ==========================================================
#
# Enter first number: 100
# Enter second number: 200
#
#
# ==========================================================
# SAMPLE OUTPUT 2
# ==========================================================
#
# Output:
# 100 200 125
#
#
# ==========================================================
# SAMPLE INPUT 3
# ==========================================================
#
# Enter first number: 201
# Enter second number: 210
#
#
# ==========================================================
# SAMPLE OUTPUT 3
# ==========================================================
#
# Output:
# 201 210 89
#
#
# ==========================================================
# SAMPLE INPUT 4
# ==========================================================
#
# Enter first number: 900
# Enter second number: 1000
#
#
# ==========================================================
# SAMPLE OUTPUT 4
# ==========================================================
#
# Output:
# 900 1000 174
#
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Read two integers i and j.
# 2. For every number between i and j:
#       Calculate its cycle length.
# 3. Cycle Length Rules:
#       If n is even -> n = n / 2
#       If n is odd  -> n = 3n + 1
# 4. Continue until n becomes 1.
# 5. Count total numbers generated.
# 6. Find maximum cycle length.
# 7. Display result.
#
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Input i and j
# Step 3: For each number from i to j
# Step 4: While n != 1
#             If n is even
#                 n = n / 2
#             Else
#                 n = 3n + 1
#             Increment count
# Step 5: Store maximum cycle length
# Step 6: Print i, j and max cycle length
# Step 7: Stop
#
#
# ==========================================================
# EXAMPLE
# ==========================================================
#
# For n = 22
#
# 22 → 11 → 34 → 17 → 52 → 26
# → 13 → 40 → 20 → 10 → 5
# → 16 → 8 → 4 → 2 → 1
#
# Cycle Length = 16
#
#
# ==========================================================
# RESULT
# ==========================================================
#
# The maximum cycle length between the given
# numbers was successfully computed using the
# 3n + 1 (Collatz) algorithm.
#
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. What is the 3n + 1 algorithm?
#
# Ans:
# If n is even:
#       n = n / 2
#
# If n is odd:
#       n = 3n + 1
#
# Repeat until n becomes 1.
#
#
# Q2. What is Cycle Length?
#
# Ans:
# Cycle length is the total number of values
# generated until the sequence reaches 1,
# including the starting number.
#
#
# Q3. Give an example of the 3n + 1 algorithm.
#
# Ans:
# Starting with 6:
#
# 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# Cycle Length = 9
#
#
# Q4. What is the Collatz Conjecture?
#
# Ans:
# It states that every positive integer
# eventually reaches 1 when the 3n + 1
# process is repeatedly applied.
#
#
# Q5. Has the Collatz Conjecture been proven?
#
# Ans:
# No. It has been tested for very large numbers
# but has not been mathematically proven.
#
#
# Q6. What is the time complexity?
#
# Ans:
# O(n × k)
#
# where:
# n = numbers in the range
# k = average cycle length
#
# ==========================================================