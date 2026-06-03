from collections import Counter

value_map = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12,
    'K': 13, 'A': 14
}

def evaluate_hand(hand):
    values = sorted([value_map[card[0]] for card in hand])
    suits = [card[1] for card in hand]

    count = Counter(values)
    freq = sorted(count.values(), reverse=True)

    flush = len(set(suits)) == 1
    straight = values == list(range(values[0], values[0] + 5))

    if flush and values == [10, 11, 12, 13, 14]:
        return (10, max(values))

    if flush and straight:
        return (9, max(values))

    if freq == [4, 1]:
        four = max(count, key=lambda x: count[x])
        return (8, four)

    if freq == [3, 2]:
        three = max(count, key=lambda x: count[x])
        return (7, three)

    if flush:
        return (6, max(values))

    if straight:
        return (5, max(values))

    if freq == [3, 1, 1]:
        three = max(count, key=lambda x: count[x])
        return (4, three)

    if freq == [2, 2, 1]:
        pairs = sorted([v for v, c in count.items() if c == 2],
                       reverse=True)
        return (3, pairs)

    if freq == [2, 1, 1, 1]:
        pair = max(v for v, c in count.items() if c == 2)
        return (2, pair)

    return (1, max(values))

print("Enter Hand 1 (5 cards):")
hand1 = input().split()

print("Enter Hand 2 (5 cards):")
hand2 = input().split()

rank1 = evaluate_hand(hand1)
rank2 = evaluate_hand(hand2)

if rank1 > rank2:
    print("Hand 1 wins")
elif rank2 > rank1:
    print("Hand 2 wins")
else:
    print("Tie")






# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter Hand 1 (5 cards):
# 2H 3D 5S 9C KD
#
# Enter Hand 2 (5 cards):
# 2C 3H 4S 8C AH
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# Hand 2 wins
#
# Reason:
# Both hands are High Card hands.
# Hand 1 highest card = King (K)
# Hand 2 highest card = Ace (A)
# Since Ace > King, Hand 2 wins.
# ==========================================================