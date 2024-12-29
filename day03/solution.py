import re

from read_file.read_file import read_file

memory = "".join(read_file("input.txt"))

matches_part_1 = re.findall(r"mul\((\d+),(\d+)\)", memory)
part_1 = sum(int(l) * int(r) for (l, r) in matches_part_1)
print(f"Part 1: {part_1}")

matches_part_2 = re.findall(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", memory)
part_2 = 0
enabled = True
for (operation, l, r) in matches_part_2:
    match operation:
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            if enabled:
                part_2 += int(l) * int(r)

print(f"Part 2: {part_2}")
