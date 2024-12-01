from collections import Counter

from read_file.read_file import read_file

lines = read_file("input.txt")

left = []
right = []

for line in lines:
    a, b = line.split("   ")
    left.append(int(a))
    right.append(int(b))

left.sort()
right.sort()

part_1 = sum(abs(a - b) for (a, b) in zip(left, right))
print(f"Part 1: {part_1}")

right_counter = Counter(right)

part_2 = sum(element * right_counter[element] for element in left)
print(f"Part 2: {part_2}")

