# Function for flood fill
def flood_fill(grid, x, y, color):

    rows = len(grid)
    cols = len(grid[0])

    # Old color at selected position
    old = grid[y][x]

    # If same color, stop
    if old == color:
        return

    # Queue for BFS
    queue = [(y, x)]

    # Change starting color
    grid[y][x] = color

    # Repeat until queue becomes empty
    while queue:

        r, c = queue.pop(0)

        # Check top, bottom, left, right
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:

            nr = r + dr
            nc = c + dc

            # Boundary checking
            if 0 <= nr < rows and 0 <= nc < cols:

                # Fill same old color
                if grid[nr][nc] == old:

                    grid[nr][nc] = color
                    queue.append((nr, nc))


# Create empty grid
grid = []

print("Graphical Editor Started")

while True:

    cmd = input("Enter command: ").split()

    # Exit program
    if cmd[0] == 'X':
        break

    # Create image
    elif cmd[0] == 'I':

        m = int(cmd[1])   # columns
        n = int(cmd[2])   # rows

        grid = [['O' for i in range(m)] for j in range(n)]

    # Color one pixel
    elif cmd[0] == 'L':

        x = int(cmd[1]) - 1
        y = int(cmd[2]) - 1
        color = cmd[3]

        grid[y][x] = color

    # Draw vertical line
    elif cmd[0] == 'V':

        x = int(cmd[1]) - 1
        y1 = int(cmd[2]) - 1
        y2 = int(cmd[3]) - 1
        color = cmd[4]

        for i in range(y1, y2 + 1):
            grid[i][x] = color

    # Draw horizontal line
    elif cmd[0] == 'H':

        x1 = int(cmd[1]) - 1
        x2 = int(cmd[2]) - 1
        y = int(cmd[3]) - 1
        color = cmd[4]

        for i in range(x1, x2 + 1):
            grid[y][i] = color

    # Flood fill
    elif cmd[0] == 'F':

        x = int(cmd[1]) - 1
        y = int(cmd[2]) - 1
        color = cmd[3]

        flood_fill(grid, x, y, color)

    # Show image
    elif cmd[0] == 'S':

        print("\nImage:")

        for row in grid:
            print("".join(row))