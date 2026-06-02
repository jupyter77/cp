# ==========================================================
# Experiment No. 19
# Title: Shell Sort Simulation
# Aim:
# To sort an array using Shell Sort Algorithm.
# ==========================================================

# Taking number of elements from user
n = int(input("Enter number of elements: "))

# Taking array elements
arr = list(map(int, input("Enter array elements: ").split()))

# Initial gap is half of array size
gap = n // 2

# Continue until gap becomes 0
while gap > 0:

    # Traverse elements from gap to end
    for i in range(gap, n):

        # Store current element
        temp = arr[i]

        # Compare with previous gap elements
        j = i

        # Shift larger elements to the right
        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j -= gap

        # Insert element at correct position
        arr[j] = temp

    # Reduce gap for next pass
    gap //= 2

# Display sorted array
print("\nSorted Array:")
for num in arr:
    print(num, end=" ")



# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter number of elements: 8
# Enter array elements: 9 8 3 7 5 6 4 1
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# Sorted Array:
# 1 3 4 5 6 7 8 9
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Read the number of elements (n).
# 2. Read array elements from the user.
# 3. Set initial gap = n // 2.
# 4. Compare elements that are gap positions apart.
# 5. Shift larger elements to the right.
# 6. Insert current element at its correct position.
# 7. Reduce the gap by half after each pass.
# 8. Repeat until gap becomes 0.
# 9. Display the sorted array.
#
# Shell Sort is an improved version of Insertion Sort.
# Instead of comparing adjacent elements only,
# it compares elements separated by a gap.
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Input number of elements n
# Step 3: Input array elements
# Step 4: Set gap = n // 2
# Step 5: While gap > 0
#            Compare elements gap distance apart
#            Shift elements if required
#            Insert element at correct position
#            Reduce gap = gap // 2
# Step 6: Print sorted array
# Step 7: Stop
#
# ==========================================================
# RESULT
# ==========================================================
#
# The given array was successfully sorted using
# the Shell Sort algorithm.
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. What is Shell Sort?
# Ans:
# Shell Sort is an improved version of Insertion Sort
# that compares elements separated by a gap.
#
# Q2. What is a Gap Sequence?
# Ans:
# Gap Sequence is the series of gap values used during
# Shell Sort. The gap gradually reduces until it becomes 1.
#
# Q3. What is the Time Complexity of Shell Sort?
# Ans:
# Best Case  : O(n log n)
# Average Case: O(n^1.5)
# Worst Case : O(n^2)
#
# ==========================================================