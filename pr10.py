# ==========================================================
# Experiment No. 10
# Title : Contest Scoreboard
#
# Aim :
# To simulate programming contest scoring and generate
# the correct ranking of teams based on problems solved
# and penalty time.
# ==========================================================

# ----------------------------------------------------------
# PROGRAM EXPLANATION
# ----------------------------------------------------------
#
# In programming contests, teams are ranked using:
#
# 1. Problems Solved (Higher is Better)
# 2. Penalty Time (Lower is Better)
# 3. Team Number (Lower is Better if tie occurs)
#
# Ranking Rules:
#
# Rule 1:
# Team with more solved problems gets higher rank.
#
# Rule 2:
# If solved problems are equal,
# lower penalty time gets higher rank.
#
# Rule 3:
# If both are equal,
# lower team number gets higher rank.
#
# Python sorting is used to generate rankings.
#
# ----------------------------------------------------------
# ALGORITHM
# ----------------------------------------------------------
#
# 1. Input number of teams.
# 2. Input team details:
#       Team Number
#       Problems Solved
#       Penalty Time
# 3. Store data in a list.
# 4. Sort teams using:
#       Problems Solved (Descending)
#       Penalty Time (Ascending)
#       Team Number (Ascending)
# 5. Display ranked scoreboard.
#
# ----------------------------------------------------------

# Input number of teams
n = int(input("Enter number of teams: "))

teams = []

# Read team data
for i in range(n):

    print(f"\nEnter details for Team {i+1}")

    team_no = int(input("Team Number: "))
    solved = int(input("Problems Solved: "))
    penalty = int(input("Penalty Time: "))

    teams.append([team_no, solved, penalty])

# ----------------------------------------------------------
# SORTING LOGIC
# ----------------------------------------------------------
#
# Sort by:
# 1. Problems Solved -> Descending (-solved)
# 2. Penalty Time -> Ascending
# 3. Team Number -> Ascending
#
# ----------------------------------------------------------

teams.sort(key=lambda x: (-x[1], x[2], x[0]))

# ----------------------------------------------------------
# DISPLAY SCOREBOARD
# ----------------------------------------------------------

print("\n========== CONTEST SCOREBOARD ==========")
print("Rank\tTeam\tSolved\tPenalty")

rank = 1

for team in teams:
    print(f"{rank}\t{team[0]}\t{team[1]}\t{team[2]}")
    rank += 1

# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter number of teams: 4
#
# Enter details for Team 1
# Team Number: 1
# Problems Solved: 2
# Penalty Time: 100
#
# Enter details for Team 2
# Team Number: 2
# Problems Solved: 3
# Penalty Time: 150
#
# Enter details for Team 3
# Team Number: 3
# Problems Solved: 2
# Penalty Time: 80
#
# Enter details for Team 4
# Team Number: 4
# Problems Solved: 1
# Penalty Time: 60
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# ========== CONTEST SCOREBOARD ==========
#
# Rank    Team    Solved  Penalty
#
# 1       2       3       150
# 2       3       2       80
# 3       1       2       100
# 4       4       1       60
#
# ==========================================================
# RESULT
# ==========================================================
#
# Contest leaderboard was successfully generated
# using sorting and ranking logic.
#
# ==========================================================
# VIVA QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. What is the main purpose of a contest scoreboard?
#
# Answer:
# To rank contestants based on performance in a contest.
#
# ----------------------------------------------------------
#
# Q2. What is meant by "Problems Solved"?
#
# Answer:
# The number of contest problems correctly solved
# by a participant or team.
#
# ----------------------------------------------------------
#
# Q3. What type of sorting technique can be used?
#
# Answer:
# Any sorting technique such as:
# Bubble Sort
# Selection Sort
# Merge Sort
# Quick Sort
# Python's Built-in Sort
#
# ----------------------------------------------------------
#
# Q4. Where are scoreboard ranking systems used?
#
# Answer:
# Programming contests,
# Coding competitions,
# Sports tournaments,
# Online gaming leaderboards.
#
# ----------------------------------------------------------
#
# Q5. Why is penalty time used?
#
# Answer:
# To break ties between teams having the same
# number of solved problems.
#
# ----------------------------------------------------------
#
# Q6. Which team gets higher rank?
#
# Answer:
# The team with more solved problems.
#
# ----------------------------------------------------------
#
# Q7. What happens if two teams have the same
# solved problems?
#
# Answer:
# The team with lower penalty time gets
# the higher rank.
#
# ----------------------------------------------------------
#
# Q8. What data structure is used in this program?
#
# Answer:
# List.
#
# ----------------------------------------------------------
#
# Q9. What is sorting?
#
# Answer:
# Arranging data in a particular order
# such as ascending or descending.
#
# ----------------------------------------------------------
#
# Q10. Why is ranking important?
#
# Answer:
# Ranking helps identify the best-performing
# contestants in a competition.
#
# ==========================================================




