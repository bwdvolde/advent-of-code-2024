from collections import defaultdict
from functools import cmp_to_key

from read_file.read_file import read_file

lines = read_file("input.txt")

iterator = iter(lines)

required_pages = defaultdict(set)

while line := next(iterator):
    required_page, page = line.split("|")
    required_pages[page].add(required_page)

updates = []
while True:
    try:
        line = next(iterator)
        updates.append(line.split(","))
    except StopIteration:
        break


def is_in_right_order(update):
    printed_pages = set()
    for page in update:
        required_pages_in_update = {required_page for required_page in required_pages[page] if required_page in update}
        if not required_pages_in_update.issubset(printed_pages):
            return False
        printed_pages.add(page)
    return True


updates_correct_order = [update for update in updates if is_in_right_order(update)]
part_1 = sum(int(update[len(update) // 2]) for update in updates_correct_order)
print(f"Part 1: {part_1}")

updates_wrong_order = [update for update in updates if not is_in_right_order(update)]
sorted_updates_wrong_order = []
for update in updates_wrong_order:
    sorted_update = sorted(update, key=cmp_to_key(lambda a, b: -1 if a in required_pages[b] else 1))
    sorted_updates_wrong_order.append(sorted_update)

part_2 = sum(int(update[len(update) // 2]) for update in sorted_updates_wrong_order)
print(f"Part 2: {part_2}")
