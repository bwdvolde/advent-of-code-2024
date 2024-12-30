from dataclasses import dataclass

from read_file.read_file import read_file

grid = read_file("input.txt")
height = len(grid)
width = len(grid[0])


@dataclass(frozen=True)
class Coord:
    row: int
    col: int

    def __add__(self, other):
        return Coord(self.row + other.row, self.col + other.col)


directions = [
    Coord(-1, -1),
    Coord(-1, 0),
    Coord(-1, 1),
    Coord(0, 1),
    Coord(1, 1),
    Coord(1, 0),
    Coord(1, -1),
    Coord(0, -1),
]


def count_matches_part_1(coord: Coord) -> int:
    n_matches = 0
    for direction in directions:
        current = coord
        i = 0
        while i < 4 and 0 <= current.row < height and 0 <= current.col < width and grid[current.row][current.col] == \
                "XMAS"[i]:
            i += 1
            current += direction
        if i == 4:
            n_matches += 1
    return n_matches


def count_matches_part_2(coord: Coord) -> int:
    if coord.row in [0, height - 1] or coord.col in [0, width - 1]:
        return 0

    left_top = coord + Coord(-1, -1)
    left_bottom = coord + Coord(1, -1)
    right_top = coord + Coord(-1, 1)
    right_bottom = coord + Coord(1, 1)

    return ({grid[left_top.row][left_top.col], grid[right_bottom.row][right_bottom.col]} == {"M", "S"}
            and {grid[right_top.row][right_top.col], grid[left_bottom.row][left_bottom.col]} == {"M", "S"})


x_coords = [
    Coord(row, col)
    for row in range(len(grid))
    for col in range(len(grid[row]))
    if grid[row][col] == "X"
]

part_1 = sum(count_matches_part_1(coord) for coord in x_coords)

print(f"Part 1: {part_1}")

a_coords = [
    Coord(row, col)
    for row in range(len(grid))
    for col in range(len(grid[row]))
    if grid[row][col] == "A"
]

part_2 = sum(count_matches_part_2(coord) for coord in a_coords)

print(f"Part 2: {part_2}")
