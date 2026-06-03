# Enter number of elements
n = int(input("Enter number of elements: "))

# Enter sequence
arr = list(map(int, input("Enter numbers: ").split()))

# Set to store differences
diff = set()

# Find adjacent differences
for i in range(n - 1):

    d = abs(arr[i] - arr[i + 1])

    # Add difference into set
    diff.add(d)

# Compare with numbers from 1 to n-1
if diff == set(range(1, n)):

    print("Jolly")

else:

    print("Not Jolly")