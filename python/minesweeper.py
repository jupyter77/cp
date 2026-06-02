# ==========================================================
# Experiment No. 2
# Title: Minesweeper
# Aim:
# To generate a Minesweeper field showing the number
# of mines adjacent to each cell in an M x N grid.
# ==========================================================

# Input rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the grid row by row:")
grid = []

# Read grid
for i in range(rows):
    grid.append(input())

# Create result grid
result = [['0' for j in range(cols)] for i in range(rows)]

# Directions for 8 neighboring cells
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

# Traverse every cell
for i in range(rows):
    for j in range(cols):

        # If current cell contains a mine
        if grid[i][j] == '*':
            result[i][j] = '*'

        else:
            count = 0

            # Check all 8 neighbors
            for dx, dy in directions:

                ni = i + dx
                nj = j + dy

                # Boundary check
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == '*':
                        count += 1

            result[i][j] = str(count)

# Display final field
print("\nMinesweeper Field:")

for row in result:
    print("".join(row))


# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter number of rows: 4
# Enter number of columns: 4
#
# *...
# ....
# .*..
# ....
#
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# Minesweeper Field:
#
# *211
# 12*1
# 12*1
# 0111
#
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Read number of rows and columns.
# 2. Read the Minesweeper grid.
# 3. Create a result matrix.
# 4. Traverse every cell.
# 5. If cell contains a mine (*),
#    place * in result.
# 6. Otherwise count mines in all
#    8 neighboring positions.
# 7. Store count in result matrix.
# 8. Display final Minesweeper board.
#
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Input rows and columns
# Step 3: Read grid
# Step 4: Traverse each cell
# Step 5: If cell contains mine
#             Store '*'
#         Else
#             Count mines in 8 directions
#             Store count
# Step 6: Print result grid
# Step 7: Stop
#
#
# ==========================================================
# RESULT
# ==========================================================
#
# Successfully generated the Minesweeper field
# showing the count of adjacent mines for each cell.
#
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. How do you check for mines in all 8 directions?
# Ans:
# By using row and column offsets:
# (-1,-1), (-1,0), (-1,1),
# (0,-1), (0,1),
# (1,-1), (1,0), (1,1)
#
#
# Q2. What data structure is used to store the grid?
# Ans:
# A 2D list (matrix) is used.
#
#
# Q3. How do you handle boundary cells?
# Ans:
# By checking:
#
# 0 <= row < rows
# 0 <= col < cols
#
# before accessing a neighbor cell.
#
#
# Q4. Can this program be extended to dynamic mine placement?
# Ans:
# Yes. Mines can be placed randomly using
# Python's random module.
#
#
# Q5. What is the time complexity of this solution?
# Ans:
# O(M × N)
#
# where:
# M = number of rows
# N = number of columns
#
# Each cell checks at most 8 neighbors.
#
# ==========================================================