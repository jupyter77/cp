# ==========================================================
# Experiment No. 11
# Title : WERTYU Keyboard Mapping
#
# Aim :
# To decode a message typed with the keyboard shifted
# one position to the right.
# ==========================================================

# Store the keyboard layout in a single string
# Every character will be replaced by the key
# immediately to its left.
keyboard = "1234567890-=WERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

# Take the mistyped message as input
message = input("Enter the mistyped message: ")

# Create an empty string to store decoded message
decoded = ""

# Process each character in the input message
for ch in message:

    # If character is a space,
    # keep it unchanged
    if ch == " ":
        decoded += " "

    else:
        # Find position of current character
        index = keyboard.find(ch)

        # Replace it with the character
        # immediately to its left
        decoded += keyboard[index - 1]

# Display corrected message
print("\nDecoded Message:")
print(decoded)

# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# O S, GOMR YPFSU
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# I AM FINE TODAY.
#
# ==========================================================
# RESULT
# ==========================================================
#
# Corrected text displayed successfully by
# mapping each character to its left neighbor
# on the QWERTY keyboard.
#



# Explanation 

# keyboard string stores all keys in QWERTY order

# User enters the mistyped text

# Each character is checked one by one

# If the character is a space,
# it is copied directly to the result

# Otherwise, its position is found
# in the keyboard string

# The previous character (left neighbor)
# is selected and added to the decoded message

# Finally, the corrected message is displayed



# ==========================================================
# VIVA QUESTIONS & ANSWERS
# ==========================================================

# Q1. How does character mapping help in solving this problem?
# Answer:
# Character mapping helps by replacing each incorrect
# character with its corresponding correct character
# based on the keyboard layout.

# ----------------------------------------------------------

# Q2. Why do we shift characters to the left instead of the right?
# Answer:
# The message was typed with hands shifted one key
# to the right, so each character must be moved
# one position to the left to recover the intended text.

# ----------------------------------------------------------

# Q3. What happens if a character is already at the leftmost position?
# Answer:
# Such characters are not included in the input as per
# the problem statement. Otherwise, special handling
# would be required.

# ----------------------------------------------------------

# Q4. What data structure is used in this program?
# Answer:
# A string is used to store the keyboard layout and
# perform character mapping.

# ----------------------------------------------------------

# Q5. Why are spaces not modified?
# Answer:
# Spaces are not keyboard characters that need correction,
# so they are copied directly to the output.

# ----------------------------------------------------------

# Q6. What is keyboard mapping?
# Answer:
# Keyboard mapping is the process of replacing one key
# with another according to a predefined relationship.

# ----------------------------------------------------------

# Q7. What is the purpose of the find() function?
# Answer:
# The find() function returns the index position of a
# character inside the keyboard layout string.

# ----------------------------------------------------------

# Q8. Can this program decode multiple words?
# Answer:
# Yes, because spaces are preserved and every character
# is processed individually.

# ----------------------------------------------------------

# Q9. What is the time complexity of this program?
# Answer:
# The time complexity is O(n), where n is the length
# of the input string.

# ----------------------------------------------------------

# Q10. What is the main objective of this experiment?
# Answer:
# To decode a mistyped message by replacing each
# character with the key immediately to its left
# on a QWERTY keyboard.
# ==========================================================