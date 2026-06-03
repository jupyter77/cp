def is_jolly(sequence):
    n = len(sequence)

    if n == 1:
        return True

    diffs = set()

    for i in range(n - 1):
        diff = abs(sequence[i + 1] - sequence[i])

        if 1 <= diff <= n - 1:
            diffs.add(diff)

    return len(diffs) == n - 1


# Input
n = int(input())
sequence = list(map(int, input().split()))

if is_jolly(sequence):
    print("Jolly")
else:
    print("Not jolly")