# ==========================================================
# Experiment No. 12
# Title : Where's Waldorf? (Word Search)
# Aim :
# To find the starting position of words in a grid
# using multi-directional search.
# ==========================================================

# Input number of rows and columns
m, n = map(int, input("Enter rows and columns: ").split())

# Create empty grid list
grid = []

# Read grid rows and convert to lowercase
for i in range(m):
    row = input().lower()
    grid.append(row)

# Input number of words to search
k = int(input("Enter number of words: "))

# ----------------------------------------------------------
# Define 8 possible search directions
#
# (-1,-1) Up-Left
# (-1, 0) Up
# (-1, 1) Up-Right
# ( 0,-1) Left
# ( 0, 1) Right
# ( 1,-1) Down-Left
# ( 1, 0) Down
# ( 1, 1) Down-Right
# ----------------------------------------------------------

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

# ----------------------------------------------------------
# Function to check whether a word exists
# starting from a specific position
# ----------------------------------------------------------

def search_word(row, col, word):

    # Check all 8 directions
    for dr, dc in directions:

        r = row
        c = col

        matched = True

        # Check every character of the word
        for ch in word:

            # Check boundaries
            if r < 0 or r >= m or c < 0 or c >= n:
                matched = False
                break

            # Character mismatch
            if grid[r][c] != ch:
                matched = False
                break

            # Move in current direction
            r += dr
            c += dc

        # Word found
        if matched:
            return True

    return False

# ----------------------------------------------------------
# Search each word
# ----------------------------------------------------------

for _ in range(k):

    # Read word and convert to lowercase
    word = input().lower()

    found = False

    # Traverse every cell of the grid
    for i in range(m):

        if found:
            break

        for j in range(n):

            # First letter matched
            if grid[i][j] == word[0]:

                # Check all directions
                if search_word(i, j, word):

                    # Output position (1-based indexing)
                    print(i + 1, j + 1)

                    found = True
                    break

# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# 3 4
# abcd
# efgh
# ijkl
# 2
# abc
# gh
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# 1 1
# 2 3
#
# ==========================================================
# RESULT
# ==========================================================
#
# Word positions located successfully using
# multi-directional word search.
#



#Program Explanation (Comments)

# Take number of rows and columns

# Read grid characters row by row

# Convert grid to lowercase for
# case-insensitive comparison

# Input number of words to search

# Store all 8 search directions

# Create function to search word
# from a starting position

# Check every direction

# Compare each character of word

# Check grid boundaries

# If all characters match,
# return True

# Otherwise return False

# For each word:
#   Convert to lowercase
#   Traverse entire grid
#   Find first letter match
#   Search in all 8 directions

# Print starting position
# using 1-based indexing




# ==========================================================
# VIVA QUESTIONS & ANSWERS
# ==========================================================

# Q1. What is meant by case-insensitive comparison?
# Answer:
# Uppercase and lowercase letters are treated
# as the same character during comparison.

# ----------------------------------------------------------

# Q2. Why do we check in 8 directions?
# Answer:
# A word can appear horizontally, vertically,
# or diagonally in any direction.

# ----------------------------------------------------------

# Q3. What data structure is used to store the grid?
# Answer:
# A 2D array (list of strings).

# ----------------------------------------------------------

# Q4. What is the time complexity of this approach?
# Answer:
# O(m × n × L × 8)
# where:
# m = rows
# n = columns
# L = length of word

# ----------------------------------------------------------

# Q5. Why is the grid converted to lowercase?
# Answer:
# To perform case-insensitive matching.

# ----------------------------------------------------------

# Q6. What is pattern searching?
# Answer:
# Finding the occurrence of a word or sequence
# inside a larger collection of data.

# ----------------------------------------------------------

# Q7. Can a word be searched diagonally?
# Answer:
# Yes, diagonal directions are included.

# ----------------------------------------------------------

# Q8. Why are row and column offsets used?
# Answer:
# They help move through the grid in different
# directions efficiently.

# ----------------------------------------------------------

# Q9. What is a 2D array?
# Answer:
# A data structure consisting of rows and columns.

# ----------------------------------------------------------

# Q10. What is the objective of this experiment?
# Answer:
# To locate words in a character grid using
# multi-directional searching techniques.
# ==========================================================