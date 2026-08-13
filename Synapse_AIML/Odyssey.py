word = "ITHACA"

required = {}
for ch in word:
    if ch in required:
        required[ch] += 1
    else:
        required[ch] = 1

count = {}
for ch in required:
    count[ch] = 0

print("Enter letters one per line. Press Enter on a blank line when done.")

sequence = []
while True:
    line = input()
    if line.strip() == "":
        break
    sequence.append(line.strip())

answer = -1
total = 0

for ch in sequence:
    ch = ch.upper()
    total += 1

    if ch in count:
        count[ch] += 1

    possible = True
    for letter in required:
        if count[letter] < required[letter]:
            possible = False
            break

    if possible:
        answer = total
        break

if answer == -1:
    print("The collected letters cannot form the word.", -1)
else:
    print("The collected letters can form the word ITHACA after", answer, "letters.")