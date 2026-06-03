# ==========================================================
# Experiment No. 09
# Title : Erdos Numbers Using Graph Traversal
# Aim :
# To compute the Erdos number of authors using
# Breadth-First Search (BFS).
# ==========================================================

# ----------------------------------------------------------
# PROGRAM EXPLANATION
# ----------------------------------------------------------
#
# Erdos Number represents the collaborative distance
# between an author and the famous mathematician
# Paul Erdos.
#
# Erdos himself has Erdos Number = 0
#
# Direct co-author of Erdos:
# Erdos Number = 1
#
# Co-author of Erdos's co-author:
# Erdos Number = 2
#
# and so on...
#
# This problem can be represented as a graph:
#
# Vertices (Nodes) = Authors
# Edges = Co-authorship relationships
#
# To find the shortest collaboration distance,
# Breadth-First Search (BFS) is used.
#
# BFS explores nodes level by level.
#
# ----------------------------------------------------------
# ALGORITHM
# ----------------------------------------------------------
#
# 1. Represent each author as a node.
# 2. Add edges between co-authors.
# 3. Start BFS from "Erdos".
# 4. Assign Erdos Number = 0 to Erdos.
# 5. Visit all neighbors.
# 6. Neighbor Erdos Number =
#    Current Author Erdos Number + 1
# 7. Continue until queue becomes empty.
# 8. Display Erdos Numbers.
#
# ----------------------------------------------------------

from collections import deque

# Input number of authors and collaborations
n, m = map(int, input(
    "Enter number of authors and collaborations: "
).split())

# Graph representation using dictionary
graph = {}

print("Enter co-author pairs:")

# Read collaborations
for i in range(m):

    a, b = input().split()

    if a not in graph:
        graph[a] = []

    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

# ----------------------------------------------------------
# BFS Traversal
# ----------------------------------------------------------

erdos_number = {}

queue = deque()

source = "Erdos"

queue.append(source)

erdos_number[source] = 0

while queue:

    current = queue.popleft()

    if current in graph:

        for neighbor in graph[current]:

            if neighbor not in erdos_number:

                erdos_number[neighbor] = \
                    erdos_number[current] + 1

                queue.append(neighbor)

# ----------------------------------------------------------
# Display Result
# ----------------------------------------------------------

print("\nErdos Numbers:")

for author in erdos_number:
    print(author, "->", erdos_number[author])

# ==========================================================
# SAMPLE INPUT
# ==========================================================
#
# Enter number of authors and collaborations: 4 3
#
# Enter co-author pairs:
# Erdos Alice
# Alice Bob
# Bob Charlie
#
# ==========================================================
# SAMPLE OUTPUT
# ==========================================================
#
# Erdos Numbers:
#
# Erdos -> 0
# Alice -> 1
# Bob -> 2
# Charlie -> 3
#
# ==========================================================
# RESULT
# ==========================================================
#
# Erdos numbers were successfully calculated
# using Breadth-First Search (BFS).
#
# ==========================================================
# VIVA QUESTIONS AND ANSWERS
# ==========================================================
#
# Q1. What is BFS?
#
# Answer:
# Breadth-First Search (BFS) is a graph traversal
# algorithm that explores nodes level by level
# using a queue.
#
# ----------------------------------------------------------
#
# Q2. What is Graph Traversal?
#
# Answer:
# Graph traversal is the process of visiting all
# nodes in a graph systematically.
#
# ----------------------------------------------------------
#
# Q3. Why is BFS used for Erdos Numbers?
#
# Answer:
# BFS finds the shortest path in an unweighted graph.
#
# ----------------------------------------------------------
#
# Q4. What data structure is used in BFS?
#
# Answer:
# Queue.
#
# ----------------------------------------------------------
#
# Q5. What happens if an author is not connected
# to Erdos?
#
# Answer:
# Its Erdos Number is undefined (infinite).
#
# ----------------------------------------------------------
#
# Q6. What is a graph?
#
# Answer:
# A graph is a collection of vertices (nodes)
# and edges connecting them.
#
# ----------------------------------------------------------
#
# Q7. What are vertices in this problem?
#
# Answer:
# Authors.
#
# ----------------------------------------------------------
#
# Q8. What are edges in this problem?
#
# Answer:
# Co-authorship relationships.
#
# ----------------------------------------------------------
#
# Q9. What is the time complexity of BFS?
#
# Answer:
# O(V + E)
# where V = Vertices and E = Edges.
#
# ----------------------------------------------------------
#
# Q10. What are applications of BFS?
#
# Answer:
# 1. Social Networks
# 2. Shortest Path Problems
# 3. Recommendation Systems
# 4. Network Analysis
#
# ==========================================================