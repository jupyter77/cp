# Experiment No. 11
# WERTYU Keyboard Mapping

keyboard = "1234567890-=WERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

message = input("Enter the mistyped message: ")

decoded = ""

for ch in message:
    if ch == ' ':
        decoded += ' '
    else:
        index = keyboard.find(ch)

        if index > 0:
            decoded += keyboard[index - 1]
        else:
            decoded += ch

print("\nDecoded Message:")
print(decoded)

# Sample Input:
# O S, GOMR YPFSU
#
# Sample Output:
# I AM FINE TODAY.