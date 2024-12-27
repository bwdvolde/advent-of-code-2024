from itertools import pairwise

from read_file.read_file import read_file

lines = read_file("input.txt")

reports = []
for line in lines:
    reports.append(list(map(int, line.split(" "))))

print(reports)

def is_safe_part_1(report):
    differences = [a - b for (a, b) in pairwise(report)]

    is_all_decreasing_or_increasing = all(difference < 0 for difference in differences) or all(difference > 0 for difference in differences)
    is_small_difference = all(1 <= abs(difference) <= 3 for difference in differences)
    return is_all_decreasing_or_increasing and is_small_difference


def is_safe_part_2(report):
    if is_safe_part_1(report):
        return True

    for i, _ in enumerate(report):
        report_without_level = report.copy()
        del report_without_level[i]
        if is_safe_part_1(report_without_level):
            return True
    return False

part_1 = len(list(filter(is_safe_part_1, reports)))
print(f"Part 1: {part_1}")

part_2 = len(list(filter(is_safe_part_2, reports)))
print(f"Part 2: {part_2}")
