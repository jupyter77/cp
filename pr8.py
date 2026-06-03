# ==========================================================
# Experiment No. 08
# Title : Stuck 'em Up (Card Shuffling Simulation)
# Aim :
# To simulate card shuffling using permutations.
# ==========================================================

# ----------------------------------------------------------
# PROGRAM EXPLANATION
# ----------------------------------------------------------
#
# A deck of cards is represented using a list.
#
# Each shuffle is represented as a permutation.
#
# A permutation specifies where each card should move.
#
# Example:
# Deck = [A, B, C, D]
#
# Permutation = [2, 1, 4, 3]
#
# After applying permutation:
# New Deck = [B, A, D, C]
#
# Multiple shuffles can be applied one after another.
#
# ----------------------------------------------------------
# ALGORITHM
# ----------------------------------------------------------
#
# 1. Create a deck of 52 cards.
# 2. Read number of shuffle permutations.
# 3. Store each permutation.
# 4. Read sequence of shuffles to apply.
# 5. For each shuffle:
#       Create temporary deck.
#       Rearrange cards according to permutation.
#       Copy temporary deck back.
# 6. Print final deck.
#
# ----------------------------------------------------------

# Create suits
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

# Create ranks
ranks = [
    "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "Jack",
    "Queen", "King", "Ace"
]

# ----------------------------------------------------------
# Create standard deck of 52 cards
# ----------------------------------------------------------
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(rank + " of " + suit)

# Number of cards
n = 52

# ----------------------------------------------------------
# Input number of shuffle permutations
# ----------------------------------------------------------
shuffle_count = int(input("Enter number of shuffles: "))

# Store permutations
permutations = []

print("\nEnter permutations:")

for i in range(shuffle_count):

    perm = list(map(int, input().split()))

    # Convert to 0-based indexing
    perm = [x - 1 for x in perm]

    permutations.append(perm)

# ----------------------------------------------------------
# Input number of shuffle operations
# ----------------------------------------------------------
sequence_count = int(
    input("\nEnter number of shuffle operations: ")
)

# ----------------------------------------------------------
# Apply shuffle sequence
# ----------------------------------------------------------
print("Enter sequence of shuffles:")

for i in range(sequence_count):

    s = int(input()) - 1

    temp = [""] * n

    for j in range(n):
        temp[j] = deck[permutations[s][j]]

    deck = temp

# ----------------------------------------------------------
# Display final deck
# ----------------------------------------------------------
print("\nFinal Deck:\n")

for card in deck:
    print(card)



# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter number of shuffles: 1
#
# Enter permutations:
# 2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
# Enter number of shuffle operations: 1
#
# Enter sequence of shuffles:
# 1
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# Final Deck:
#
# 3 of Clubs
# 2 of Clubs
# 4 of Clubs
# 5 of Clubs
# 6 of Clubs
# 7 of Clubs
# 8 of Clubs
# 9 of Clubs
# 10 of Clubs
# Jack of Clubs
# Queen of Clubs
# King of Clubs
# Ace of Clubs
# 2 of Diamonds
# ...
# Ace of Spades
#
# ==========================================================
# RESULT
# ==========================================================
#
# The deck was successfully shuffled using
# permutation-based simulation.
#
# ==========================================================


# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# This program simulates card shuffling using permutations.
#
# A standard deck contains 52 cards:
# - 13 card values (2 to Ace)
# - 4 suits (Clubs, Diamonds, Hearts, Spades)
#
# The deck is stored as a list where each element
# represents one card.
#
# Example:
# 2 of Clubs
# 3 of Clubs
# ...
# Ace of Spades
#
# ----------------------------------------------------------
# What is a Permutation?
# ----------------------------------------------------------
#
# A permutation is an arrangement of positions.
#
# It tells where each card should move after shuffling.
#
# Example:
#
# Original Deck:
# [A, B, C, D]
#
# Permutation:
# [2, 1, 4, 3]
#
# New Deck:
# [B, A, D, C]
#
# Thus permutations are used to simulate shuffling.
#
# ----------------------------------------------------------
# Working of the Program
# ----------------------------------------------------------
#
# Step 1:
# Create a standard deck of 52 cards.
#
# Step 2:
# Read the number of shuffle patterns.
#
# Step 3:
# Store each shuffle pattern (permutation array).
#
# Step 4:
# Read the sequence of shuffles to apply.
#
# Step 5:
# For every shuffle:
#   - Create a temporary deck.
#   - Rearrange cards according to permutation.
#   - Copy temporary deck back to original deck.
#
# Step 6:
# Print the final arrangement of cards.
#
# ----------------------------------------------------------
# Data Structures Used
# ----------------------------------------------------------
#
# List:
# Used to store the deck of cards.
#
# Nested List:
# Used to store multiple permutations.
#
# ----------------------------------------------------------
# Functions of Major Variables
# ----------------------------------------------------------
#
# suits
# Stores the four suits.
#
# ranks
# Stores card values.
#
# deck
# Stores the complete deck of cards.
#
# permutations
# Stores all shuffle patterns.
#
# temp
# Temporary deck used while shuffling.
#
# ----------------------------------------------------------
# Time Complexity
# ----------------------------------------------------------
#
# Creating Deck:
# O(52)
#
# Applying One Shuffle:
# O(52)
#
# Applying K Shuffles:
# O(52 × K)
#
# ----------------------------------------------------------
# Space Complexity
# ----------------------------------------------------------
#
# O(52)
#
# Because a temporary deck of 52 cards is used.
#
# ----------------------------------------------------------
# Applications
# ----------------------------------------------------------
#
# 1. Card game simulations
# 2. Randomization algorithms
# 3. Cryptography
# 4. Data shuffling in Machine Learning
# 5. Gaming systems
#
# ==========================================================


# ==========================================================
# VIVA QUESTIONS AND ANSWERS
# ==========================================================

# Q1. What is a permutation?
#
# Answer:
# A permutation is an arrangement of elements in a
# specific order. In this experiment, permutations
# determine how card positions change after shuffling.

# ----------------------------------------------------------

# Q2. What is deck representation?
#
# Answer:
# Deck representation means storing all cards in a
# structured format such as an array or list where
# each position corresponds to one card.

# ----------------------------------------------------------

# Q3. Why are permutations used in shuffling?
#
# Answer:
# Permutations define how positions of cards change
# after each shuffle. They provide a mathematical way
# to simulate card shuffling.

# ----------------------------------------------------------

# Q4. What data structure is used to store the deck?
#
# Answer:
# A list (array) is used to store the deck of cards.
# Each element of the list represents one card.

# ----------------------------------------------------------

# Q5. Can this method simulate real shuffling?
#
# Answer:
# Yes. If the permutations are generated randomly,
# this method can simulate real card shuffling.

# ----------------------------------------------------------

# Additional Viva Questions
# ----------------------------------------------------------

# Q6. How many cards are present in a standard deck?
#
# Answer:
# A standard deck contains 52 cards consisting of
# 4 suits and 13 values in each suit.

# ----------------------------------------------------------

# Q7. What are the four suits in a deck?
#
# Answer:
# Clubs (C), Diamonds (D), Hearts (H), and Spades (S).

# ----------------------------------------------------------

# Q8. Why is a temporary deck used during shuffling?
#
# Answer:
# A temporary deck prevents overwriting card positions
# while rearranging cards according to the permutation.

# ----------------------------------------------------------

# Q9. Can multiple shuffles be applied?
#
# Answer:
# Yes. Multiple shuffle permutations can be applied
# sequentially to obtain the final deck arrangement.

# ----------------------------------------------------------

# Q10. What is the time complexity of one shuffle?
#
# Answer:
# O(n), where n is the number of cards in the deck.
# For a standard deck, n = 52.

# ----------------------------------------------------------

# Q11. What is the space complexity?
#
# Answer:
# O(n), because an additional temporary deck is used.

# ----------------------------------------------------------

# Q12. What are the applications of permutation-based
# shuffling?
#
# Answer:
# 1. Card game simulations
# 2. Cryptography
# 3. Randomization algorithms
# 4. Machine Learning data shuffling
# 5. Gaming systems

# ==========================================================