# ==========================================================
# Experiment No. 07
# Title : Poker Hands
# Aim :
# To design a program that evaluates and compares
# Poker hands based on standard card rankings.
# ==========================================================

# Counter is used to count occurrences of card values
from collections import Counter

# ----------------------------------------------------------
# Mapping card symbols to numeric values
# 2 is lowest and Ace is highest
# ----------------------------------------------------------
VALUE_MAP = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

# ----------------------------------------------------------
# Function to evaluate a poker hand
# Input : List containing 5 cards
# Output : Rank, card values and hand name
# ----------------------------------------------------------
def evaluate_hand(hand):

    # Extract card values and convert them into numbers
    # Example: AH -> A -> 14
    values = sorted(
        [VALUE_MAP[card[0]] for card in hand],
        reverse=True
    )

    # Extract suits
    # Example: AH -> H
    suits = [card[1] for card in hand]

    # Count occurrences of each value
    # Useful for detecting pairs, three of a kind, etc.
    value_count = Counter(values)

    # Store counts in descending order
    counts = sorted(value_count.values(), reverse=True)

    # Store unique card values
    unique_values = sorted(value_count.keys())

    # ------------------------------------------------------
    # Check for Flush
    # Flush means all cards have same suit
    # ------------------------------------------------------
    flush = len(set(suits)) == 1

    # ------------------------------------------------------
    # Check for Straight
    # Straight means consecutive card values
    # ------------------------------------------------------
    straight = False

    if len(unique_values) == 5:

        # Normal straight
        if max(unique_values) - min(unique_values) == 4:
            straight = True

        # Special case:
        # A-2-3-4-5 is also considered a straight
        if unique_values == [2, 3, 4, 5, 14]:
            straight = True
            values = [5, 4, 3, 2, 1]

    # ------------------------------------------------------
    # Determine Poker Hand Ranking
    #
    # Ranking Order:
    # Royal Flush
    # Straight Flush
    # Four of a Kind
    # Full House
    # Flush
    # Straight
    # Three of a Kind
    # Two Pair
    # One Pair
    # High Card
    # ------------------------------------------------------

    # Royal Flush
    if flush and values == [14, 13, 12, 11, 10]:
        return (9, values, "Royal Flush")

    # Straight Flush
    if flush and straight:
        return (8, values, "Straight Flush")

    # Four of a Kind
    if counts == [4, 1]:
        return (7, values, "Four of a Kind")

    # Full House
    if counts == [3, 2]:
        return (6, values, "Full House")

    # Flush
    if flush:
        return (5, values, "Flush")

    # Straight
    if straight:
        return (4, values, "Straight")

    # Three of a Kind
    if counts == [3, 1, 1]:
        return (3, values, "Three of a Kind")

    # Two Pair
    if counts == [2, 2, 1]:
        return (2, values, "Two Pair")

    # One Pair
    if counts == [2, 1, 1, 1]:
        return (1, values, "One Pair")

    # High Card
    return (0, values, "High Card")


# ----------------------------------------------------------
# Function to compare two poker hands
# ----------------------------------------------------------
def compare_hands(hand1, hand2):

    # Evaluate both hands
    rank1 = evaluate_hand(hand1)
    rank2 = evaluate_hand(hand2)

    # Compare hand ranks first
    if rank1[0] > rank2[0]:
        return "Hand 1 wins (" + rank1[2] + ")"

    elif rank2[0] > rank1[0]:
        return "Hand 2 wins (" + rank2[2] + ")"

    # If both hands have same rank
    # Compare highest cards
    else:

        if rank1[1] > rank2[1]:
            return "Hand 1 wins (" + rank1[2] + ")"

        elif rank2[1] > rank1[1]:
            return "Hand 2 wins (" + rank2[2] + ")"

        else:
            return "Tie"


# ==========================================================
# Main Program
# ==========================================================

# Input first poker hand
print("Enter Hand 1 (5 cards):")
hand1 = input().split()

# Input second poker hand
print("Enter Hand 2 (5 cards):")
hand2 = input().split()

# Compare both hands
result = compare_hands(hand1, hand2)

# Display result
print("\nResult:")
print(result)

# ==========================================================
# Sample Input
#
# Hand 1:
# 2H 3D 5S 9C KD
#
# Hand 2:
# 2C 3H 4S 8C AH
#
# Sample Output:
# Hand 2 wins (High Card)
#
# ==========================================================


# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# This program compares two Poker Hands and determines
# which hand is stronger according to standard Poker rules.
#
# ----------------------------------------------------------
# Card Representation
# ----------------------------------------------------------
# Each card consists of:
#
#   Value + Suit
#
# Examples:
#   AH = Ace of Hearts
#   KD = King of Diamonds
#   5S = Five of Spades
#   TC = Ten of Clubs
#
# Suits:
#   C = Clubs
#   D = Diamonds
#   H = Hearts
#   S = Spades
#
# Suits are NOT used for scoring.
#
# ----------------------------------------------------------
# Value Mapping
# ----------------------------------------------------------
# Card values are converted into numbers for comparison:
#
#   2  -> 2
#   3  -> 3
#   4  -> 4
#   5  -> 5
#   6  -> 6
#   7  -> 7
#   8  -> 8
#   9  -> 9
#   T  -> 10
#   J  -> 11
#   Q  -> 12
#   K  -> 13
#   A  -> 14
#
# Ace is considered the highest card.
#
# ----------------------------------------------------------
# Hand Evaluation Process
# ----------------------------------------------------------
# For each hand:
#
# 1. Extract card values.
# 2. Convert values into numeric form.
# 3. Count frequency of each card value.
# 4. Check for:
#      - Pair
#      - Two Pair
#      - Three of a Kind
#      - Straight
#      - Flush
#      - Full House
#      - Four of a Kind
#      - Straight Flush
#      - Royal Flush
# 5. Assign a rank to the hand.
#
# ----------------------------------------------------------
# Poker Hand Ranking (Highest to Lowest)
# ----------------------------------------------------------
#
# 9 -> Royal Flush
# 8 -> Straight Flush
# 7 -> Four of a Kind
# 6 -> Full House
# 5 -> Flush
# 4 -> Straight
# 3 -> Three of a Kind
# 2 -> Two Pair
# 1 -> One Pair
# 0 -> High Card
#
# ----------------------------------------------------------
# Hand Comparison
# ----------------------------------------------------------
#
# First compare hand ranks:
#
# Example:
#   Full House > Flush
#
# If both hands have same rank:
#
# Compare highest card values.
#
# Example:
#   Hand 1 : High Card King
#   Hand 2 : High Card Ace
#
# Ace is higher than King,
# therefore Hand 2 wins.
#
# ----------------------------------------------------------
# Functions Used
# ----------------------------------------------------------
#
# evaluate_hand(hand)
#     Evaluates a poker hand and returns:
#     - Rank
#     - Card values
#     - Hand name
#
# compare_hands(hand1, hand2)
#     Compares two hands and returns
#     the winning hand.
#
# ----------------------------------------------------------
# Time Complexity
# ----------------------------------------------------------
#
# Since each hand always contains only 5 cards,
# all operations are performed on a fixed size dataset.
#
# Time Complexity:
#     O(1)  (Constant Time)
#
# Space Complexity:
#     O(1)  (Constant Space)
#
# ----------------------------------------------------------
# Sample Input
# ----------------------------------------------------------
#
# Hand 1:
# 2H 3D 5S 9C KD
#
# Hand 2:
# 2C 3H 4S 8C AH
#
# ----------------------------------------------------------
# Sample Output
# ----------------------------------------------------------
#
# Hand 2 wins (High Card)
#
# Reason:
# Hand 1 highest card = King
# Hand 2 highest card = Ace
# Ace is higher than King.
#
# ==========================================================