# Function for Australian Voting
def australian_voting():

    # Number of candidates
    n = int(input("Enter number of candidates: "))

    candidates = []

    print("Enter candidate names:")

    # Store candidate names
    for i in range(n):
        candidates.append(input())

    ballots = []

    print("Enter votes (example: 1 2 3)")
    print("Press Enter on empty line to stop")

    # Take votes
    while True:

        vote = input()

        # Stop input if empty
        if vote == "":
            break

        # Convert vote numbers into list
        ballot = list(map(int, vote.split()))

        ballots.append(ballot)

    # Active candidates
    active = candidates.copy()

    # Repeat voting process
    while True:

        # Vote counter dictionary
        count = {}

        for c in active:
            count[c] = 0

        # Count votes
        for ballot in ballots:

            for choice in ballot:

                name = candidates[choice - 1]

                # Count only active candidate
                if name in active:

                    count[name] += 1
                    break

        # Total votes
        total = sum(count.values())

        # Check winner
        for c in active:

            if count[c] > total / 2:

                print("\nWinner is:", c)
                return

        # Find minimum votes
        minimum = min(count.values())

        # Check tie
        tie = True

        for c in active:

            if count[c] != minimum:
                tie = False

        if tie:

            print("\nTie between:")

            for c in active:
                print(c)

            return

        # Remove lowest candidate
        remove = []

        for c in active:

            if count[c] == minimum:
                remove.append(c)

        for c in remove:
            active.remove(c)


# Call function
australian_voting()