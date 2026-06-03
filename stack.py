# Experiment No. 08
# Stack 'em Up (Card Shuffling Simulation)

n = int(input("Enter number of cards: "))

deck = []
for i in range(1, n + 1):
    deck.append(f"Card {i}")

shuffle_count = int(input("Enter number of shuffles: "))

permutations = []

for i in range(shuffle_count):
    print("Enter permutation:")
    perm = list(map(int, input().split()))
    perm = [x - 1 for x in perm]
    permutations.append(perm)

sequence_count = int(input("Enter number of shuffle operations: "))

for i in range(sequence_count):
    s = int(input()) - 1

    temp = [None] * n

    for j in range(n):
        temp[j] = deck[permutations[s][j]]

    deck = temp

print("\nFinal Deck:")
for card in deck:
    print(card)





# SAMPLE INPUT:
#
# Enter number of cards: 10
#
# Enter number of shuffles: 1
#
# Enter permutation:
# 2 1 3 4 5 6 7 8 9 10
#
# Enter number of shuffle operations: 1
#
# Enter sequence of shuffles:
# 1
#
# SAMPLE OUTPUT:
#
# Final Deck:
# Card 2
# Card 1
# Card 3
# Card 4
# Card 5
# Card 6
# Card 7
# Card 8
# Card 9
# Card 10
#
# ==========================================================