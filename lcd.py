# Dictionary storing 7-segment patterns for digits 0-9
# Each digit has 7 positions:
#
#   ---0---
#  |       |
#  1       2
#  |       |
#   ---3---
#  |       |
#  4       5
#  |       |
#   ---6---
#
# 1 = segment ON
# 0 = segment OFF

digits_map = {
    '0': '1110111',
    '1': '0010010',
    '2': '1011101',
    '3': '1011011',
    '4': '0111010',
    '5': '1101011',
    '6': '1101111',
    '7': '1010010',
    '8': '1111111',
    '9': '1111011'
}

# Taking input from user
# Example input:
# 2 12345
# 2 = size
# 12345 = number to display

line = input("Enter size and number (e.g., 2 12345): ").strip()

# Split input into size and number
s_str, n_str = line.split()

# Convert size into integer
s = int(s_str)

# Total rows needed for LCD display
rows = 2 * s + 3

print("\nOutput:")

# Loop through each row of LCD display
for r in range(rows):

    # Stores one complete output line
    line_out = []

    # Loop through every digit entered by user
    for d in n_str:

        # Get segment pattern of current digit
        segs = digits_map[d]

        # TOP horizontal segment
        if r == 0:

            # If segment is ON print '-'
            # Else print space
            char = '-' if segs[0] == '1' else ' '

            # Add top line to output
            line_out.append(' ' + char * s + ' ')

        # UPPER vertical segments
        elif 1 <= r <= s:

            # Left vertical segment
            left = '|' if segs[1] == '1' else ' '

            # Right vertical segment
            right = '|' if segs[2] == '1' else ' '

            # Add upper middle row
            line_out.append(left + ' ' * s + right)

        # MIDDLE horizontal segment
        elif r == s + 1:

            char = '-' if segs[3] == '1' else ' '

            line_out.append(' ' + char * s + ' ')

        # LOWER vertical segments
        elif s + 2 <= r <= 2 * s + 1:

            left = '|' if segs[4] == '1' else ' '

            right = '|' if segs[5] == '1' else ' '

            line_out.append(left + ' ' * s + right)

        # BOTTOM horizontal segment
        elif r == 2 * s + 2:

            char = '-' if segs[6] == '1' else ' '

            line_out.append(' ' + char * s + ' ')

    # Print one complete LCD row
    print(' '.join(line_out))