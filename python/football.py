# ==========================================================
# Experiment No. 20
# Title: Football Tournament Ranking
# Aim:
# To rank football teams based on points and goal difference.
# ==========================================================

# Number of teams
n = int(input("Enter number of teams: "))

teams = {}

# Store team names and initialize statistics
for i in range(n):
    name = input("Enter team name: ")

    teams[name] = {
        "points": 0,
        "goals_scored": 0,
        "goals_against": 0,
        "matches": 0
    }

# Number of matches
m = int(input("Enter number of matches: "))

for i in range(m):

    print("\nMatch", i + 1)

    team1 = input("Team 1: ")
    goals1 = int(input("Goals scored by Team 1: "))

    team2 = input("Team 2: ")
    goals2 = int(input("Goals scored by Team 2: "))

    # Update goals and matches
    teams[team1]["goals_scored"] += goals1
    teams[team1]["goals_against"] += goals2
    teams[team1]["matches"] += 1

    teams[team2]["goals_scored"] += goals2
    teams[team2]["goals_against"] += goals1
    teams[team2]["matches"] += 1

    # Assign points
    if goals1 > goals2:
        teams[team1]["points"] += 3

    elif goals2 > goals1:
        teams[team2]["points"] += 3

    else:
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1


# Sort teams according to ranking rules
ranking = sorted(
    teams.items(),
    key=lambda x: (
        -x[1]["points"],

        # Goal Difference
        -(x[1]["goals_scored"] - x[1]["goals_against"]),

        # Goals Scored
        -x[1]["goals_scored"],

        # Less matches is better
        x[1]["matches"],

        # Alphabetical order
        x[0]
    )
)

print("\n===== TOURNAMENT STANDINGS =====")

for position, (team, stats) in enumerate(ranking, start=1):

    goal_difference = (
        stats["goals_scored"] -
        stats["goals_against"]
    )

    print(
        position,
        ".",
        team,
        "-",
        stats["points"],
        "Points",
        "| GD:",
        goal_difference
    )


# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter number of teams: 4
#
# Brazil
# Norway
# Morocco
# Scotland
#
# Enter number of matches: 3
#
# Match 1
# Team 1: Brazil
# Goals scored by Team 1: 2
# Team 2: Scotland
# Goals scored by Team 2: 1
#
# Match 2
# Team 1: Norway
# Goals scored by Team 1: 2
# Team 2: Morocco
# Goals scored by Team 2: 2
#
# Match 3
# Team 1: Brazil
# Goals scored by Team 1: 3
# Team 2: Morocco
# Goals scored by Team 2: 0
#
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# ===== TOURNAMENT STANDINGS =====
#
# 1 . Brazil - 6 Points | GD: 4
# 2 . Norway - 1 Points | GD: 0
# 3 . Morocco - 1 Points | GD: -3
# 4 . Scotland - 0 Points | GD: -1
#
#
# ==========================================================
# PROGRAM EXPLANATION
# ==========================================================
#
# 1. Read number of teams.
# 2. Store team details in a dictionary.
# 3. Read match results.
# 4. Update:
#       Points
#       Goals Scored
#       Goals Against
#       Matches Played
# 5. Calculate Goal Difference.
# 6. Sort teams using:
#       Points
#       Goal Difference
#       Goals Scored
#       Matches Played
#       Team Name
# 7. Display final rankings.
#
#
# ==========================================================
# ALGORITHM
# ==========================================================
#
# Step 1: Start
# Step 2: Input team names
# Step 3: Initialize team statistics
# Step 4: Input match results
# Step 5: Update goals and points
# Step 6: Calculate goal difference
# Step 7: Sort teams using ranking rules
# Step 8: Display standings
# Step 9: Stop
#
#
# ==========================================================
# RESULT
# ==========================================================
#
# Football tournament standings were successfully
# generated using multi-criteria sorting.
#
#
# ==========================================================
# VIVA VOCE QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. How are football points assigned?
# Ans:
# Win = 3 points
# Draw = 1 point
# Loss = 0 points
#
# Q2. What is Goal Difference?
# Ans:
# Goal Difference = Goals Scored - Goals Against
#
# Q3. What criteria are used to rank teams?
# Ans:
# 1. Points
# 2. Goal Difference
# 3. Goals Scored
# 4. Matches Played
# 5. Team Name
#
# Q4. Why is Goal Difference important?
# Ans:
# It helps break ties when teams have equal points.
#
# Q5. How is sorting with multiple conditions implemented in Python?
# Ans:
# Using sorted() function with a custom key.
#
# Q6. What is the time complexity of sorting?
# Ans:
# O(n log n)
#
# ==========================================================