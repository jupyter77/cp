# ==========================================================
# Experiment No. 4
# Title: Graphical Editor
# Aim:
# To simulate a simple graphical editor using a
# rectangular M x N grid where each cell is a pixel.
# ==========================================================

# Create image with default color 'O'
m = int(input("Enter number of columns: "))
n = int(input("Enter number of rows: "))

image = [['O' for j in range(m)] for i in range(n)]

while True:

    print("\nCommands:")
    print("L X Y C  -> Color a pixel")
    print("C        -> Clear image")
    print("S NAME   -> Show image")
    print("Q        -> Quit")

    command = input("\nEnter command: ").split()

    # Quit program
    if command[0] == 'Q':
        break

    # Color a single pixel
    elif command[0] == 'L':

        x = int(command[1])
        y = int(command[2])
        color = command[3]

        image[y - 1][x - 1] = color

    # Clear image
    elif command[0] == 'C':

        for i in range(n):
            for j in range(m):
                image[i][j] = 'O'

        print("Image Cleared!")

    # Show image
    elif command[0] == 'S':

        name = command[1]

        print("\n" + name)

        for row in image:
            print("".join(row))


# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter number of columns: 5
# Enter number of rows: 6
#
# L 2 3 R
# L 5 1 G
# S MyPicture
# C
# S Cleared
# Q
#
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# MyPicture
#
# OOOOG
# OOOOO
# OROOO
# OOOOO
# OOOOO
# OOOOO
#
#
# Cleared
#
# OOOOO
# OOOOO
# OOOOO
# OOOOO
# OOOOO
# OOOOO
#
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Create a 2D grid filled with 'O'.
# 2. Accept commands from the user.
# 3. 'L' command colors a pixel.
# 4. 'C' command clears the image.
# 5. 'S' command displays the image.
# 6. 'Q' command exits the program.
# 7. Update the grid according to commands.
#
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Create M x N image
# Step 3: Fill image with 'O'
# Step 4: Read command
# Step 5: If L
#             Color specified pixel
# Step 6: If C
#             Clear image
# Step 7: If S
#             Display image
# Step 8: If Q
#             Exit
# Step 9: Stop
#
#
# ==========================================================
# RESULT
# ==========================================================
#
# The graphical editor successfully simulated
# image editing operations using a 2D array.
#
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. How is the canvas represented in the program?
# Ans:
# The canvas is represented using a 2D list (matrix).
#
#
# Q2. How do you implement coloring of a pixel?
# Ans:
# By assigning a color value to a specific row
# and column position in the 2D array.
#
#
# Q3. How can you implement vertical and horizontal
# lines efficiently?
# Ans:
# Using loops to color multiple cells in the same
# row or column.
#
#
# Q4. What is a Flood Fill algorithm?
# Ans:
# Flood Fill colors all connected cells of the
# same color starting from a selected pixel.
#
#
# Q5. How is the canvas cleared?
# Ans:
# By setting every pixel back to the default
# color 'O'.
#
#
# Q6. What data structure is suitable for this application?
# Ans:
# A 2D Array (2D List) is the most suitable.
#
#
# ==========================================================
# SHORT VIVA ANSWERS (EXAM READY)
# ==========================================================
#
# 1. What is a pixel?
#    The smallest unit of an image.
#
# 2. Which data structure is used?
#    2D Array / 2D List.
#
# 3. Default color in this program?
#    O (White).
#
# 4. What is Flood Fill?
#    Filling connected regions with one color.
#
# 5. Time Complexity of clearing image?
#    O(M × N)
#
# ==========================================================