from collections import deque

# Input number of authors and collaborations
n, m = map(int, input("Enter number of authors and collaborations: ").split())

# Graph represented using dictionary
graph = {}

print("Enter co-author pairs:")

for _ in range(m):
    a, b = input().split()

    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

# BFS initialization
erdos_number = {}
q = deque()

source = "Erdos"

q.append(source)
erdos_number[source] = 0

# Breadth-First Search
while q:
    current = q.popleft()

    for neighbor in graph.get(current, []):
        if neighbor not in erdos_number:
            erdos_number[neighbor] = erdos_number[current] + 1
            q.append(neighbor)

# Display Erdos Numbers
print("\nErdos Numbers:")
for author, number in erdos_number.items():
    print(author, "->", number)

# Sample Input:
#
# 4 3
# Erdos Alice
# Alice Bob
# Bob Charlie
#
# Sample Output:
#
# Erdos -> 0
# Alice -> 1
# Bob -> 2
# Charlie -> 3