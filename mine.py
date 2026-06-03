r, c = map(int, input("Enter rows and columns: ").split())

grid = []

print("Enter the grid:")

for i in range(r):
    grid.append(input())

print("\nOutput:")

for i in range(r):

    for j in range(c):

        if grid[i][j] == '*':
            print('*', end='')

        else:

            count = 0

            for x in range(i-1, i+2):
                for y in range(j-1, j+2):

                    if 0 <= x < r and 0 <= y < c:

                        if grid[x][y] == '*':
                            count += 1

            print(count, end='')

    print()