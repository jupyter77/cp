# Experiment No. 10
# Contest Scoreboard

teams = []

# Input number of teams
n = int(input("Enter number of teams: "))

# Input team details
for i in range(n):
    team_no = int(input("Enter Team Number: "))
    solved = int(input("Enter Problems Solved: "))
    penalty = int(input("Enter Penalty Time: "))

    teams.append([team_no, solved, penalty])

# Sort teams:
# 1. Problems solved (descending)
# 2. Penalty time (ascending)
# 3. Team number (ascending)
teams.sort(key=lambda x: (-x[1], x[2], x[0]))

# Display scoreboard
print("\nContest Scoreboard")
print("Rank\tTeam\tSolved\tPenalty")

for rank, team in enumerate(teams, start=1):
    print(rank, "\t", team[0], "\t", team[1], "\t", team[2])

# Sample Input:
#
# Enter number of teams: 4
#
# Enter Team Number: 1
# Enter Problems Solved: 2
# Enter Penalty Time: 100
#
# Enter Team Number: 2
# Enter Problems Solved: 3
# Enter Penalty Time: 150
#
# Enter Team Number: 3
# Enter Problems Solved: 2
# Enter Penalty Time: 80
#
# Enter Team Number: 4
# Enter Problems Solved: 1
# Enter Penalty Time: 60
#
# Sample Output:
#
# Contest Scoreboard
# Rank    Team    Solved    Penalty
# 1       2       3         150
# 2       3       2         80
# 3       1       2         100
# 4       4       1         60