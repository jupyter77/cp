# ==========================================================
# Experiment No. 5
# Title: Australian Voting
# Aim:
# To implement the Australian Voting System
# (Instant Runoff Voting).
# ==========================================================

# Number of candidates
n = int(input("Enter number of candidates: "))

candidates = []

print("Enter candidate names:")
for i in range(n):
    candidates.append(input())

# Number of voters
voters = int(input("Enter number of voters: "))

ballots = []

print("Enter rankings (space separated candidate numbers):")
for i in range(voters):
    ballot = list(map(int, input().split()))
    ballots.append(ballot)

# List to store eliminated candidates
eliminated = [False] * n

while True:

    # Count votes
    votes = [0] * n

    for ballot in ballots:

        # Find highest-ranked non-eliminated candidate
        for choice in ballot:
            if not eliminated[choice - 1]:
                votes[choice - 1] += 1
                break

    total_votes = sum(votes)

    # Find maximum and minimum votes
    max_votes = max(votes)
    min_votes = min(v for i, v in enumerate(votes)
                    if not eliminated[i])

    # Check for winner (>50%)
    if max_votes > total_votes / 2:

        winner_index = votes.index(max_votes)

        print("\nWinner:", candidates[winner_index])
        break

    # Check for tie
    active_votes = [votes[i] for i in range(n)
                    if not eliminated[i]]

    if all(v == active_votes[0] for v in active_votes):

        print("\nTie Between:")

        for i in range(n):
            if not eliminated[i]:
                print(candidates[i])

        break

    # Eliminate candidate(s) with minimum votes
    for i in range(n):
        if not eliminated[i] and votes[i] == min_votes:
            eliminated[i] = True


# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter number of candidates: 3
#
# Enter candidate names:
# Alice
# Bob
# Charlie
#
# Enter number of voters: 4
#
# Enter rankings:
# 1 2 3
# 2 1 3
# 2 3 1
# 3 1 2
#
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# Winner: Bob
#
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Read candidate names.
# 2. Read voter rankings (ballots).
# 3. Count first-choice votes.
# 4. Check if any candidate has more than 50%.
# 5. If not, eliminate candidate(s) with
#    the lowest votes.
# 6. Redistribute votes according to next
#    preferred non-eliminated candidate.
# 7. Repeat until a winner or tie is found.
#
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Read candidate names
# Step 3: Read ballots
# Step 4: Count votes
# Step 5: Check majority (>50%)
# Step 6: If winner found, display winner
# Step 7: Else eliminate lowest candidate
# Step 8: Redistribute votes
# Step 9: Repeat Steps 4-8
# Step 10: Stop
#
#
# ==========================================================
# RESULT
# ==========================================================
#
# The winning candidate was successfully
# determined using the Australian Voting
# (Instant Runoff Voting) system.
#
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. What is the difference between plurality voting
# and instant runoff voting?
#
# Ans:
# Plurality voting selects the candidate with
# the highest votes, while Instant Runoff Voting
# repeatedly eliminates the lowest candidate and
# redistributes votes until a majority is achieved.
#
#
# Q2. Why is vote redistribution necessary?
#
# Ans:
# It ensures that votes for eliminated candidates
# are not wasted and are transferred to the next
# preferred candidate.
#
#
# Q3. What happens in case of a tie?
#
# Ans:
# If all remaining candidates have the same number
# of votes, the election is declared a tie.
#
#
# Q4. Can this algorithm handle incomplete ballots?
#
# Ans:
# Yes, with minor modifications it can skip missing
# preferences and count the next available choice.
#
#
# Q5. What is the worst-case number of rounds?
#
# Ans:
# n - 1 rounds, where n is the number of candidates.
#
#
# ==========================================================
# SHORT VIVA ANSWERS (EXAM READY)
# ==========================================================
#
# 1. What is Australian Voting?
#    A ranking-based voting system.
#
# 2. What is IRV?
#    Instant Runoff Voting.
#
# 3. When is a candidate declared winner?
#    When they receive more than 50% votes.
#
# 4. What happens to eliminated candidate votes?
#    They are transferred to the next preference.
#
# 5. Time Complexity?
#    O(V × C × R)
#
#    V = voters
#    C = candidates
#    R = rounds
#
# ==========================================================