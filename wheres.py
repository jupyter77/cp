# Experiment No. 12
# Where's Waldorf? (Word Search)

def search_word(grid, word, rows, cols):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    word = word.lower()

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] != word[0]:
                continue

            for dr, dc in directions:

                rr, cc = r, c
                found = True

                for k in range(1, len(word)):
                    rr += dr
                    cc += dc

                    if (rr < 0 or rr >= rows or
                        cc < 0 or cc >= cols or
                        grid[rr][cc] != word[k]):
                        found = False
                        break

                if found:
                    return r + 1, c + 1

    return -1, -1


rows, cols = map(int, input("Enter rows and columns: ").split())

grid = []
for _ in range(rows):
    grid.append(input().lower())

num_words = int(input("Enter number of words: "))

for _ in range(num_words):
    word = input().strip()

    row, col = search_word(grid, word, rows, cols)

    print(row, col)

# Sample Input:
#
# 3 4
# abcd
# efgh
# ijkl
# 2
# abc
# gh
#
# Sample Output:
#
# 1 1
# 2 3