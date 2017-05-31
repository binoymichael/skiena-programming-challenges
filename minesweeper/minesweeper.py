import re


def process(filename):
    with open(filename) as file:
        while True:
            line = next(file, '').strip()
            if line == "0 0": break
            match = re.match(r'(\d+) (\d+)', line)
            if match:
                rows, cols = [int(x) for x in match.groups()]
                grid = [[0 for y in range(cols + 2)] for x in range(rows + 2)]
                for x in range(rows):
                    line = next(file, '').strip()
                    row = [char if char != '.' else 0 for char in line]
                    grid[x + 1][1:-1] = row
                yield grid, rows, cols


def print_grid(grid):
    for row in grid:
        print("".join(str(v) for v in row))
    print()


def bump_adjacent(grid, x, y):
    for i in range(3):
        for j in range(3):
            if grid[x + i][y + j] != '*':
                grid[x + i][y + j] += 1


def solve(filename):
    for grid, rows, cols in process(filename):
        for x in range(rows):
            for y in range(cols):
                if grid[x + 1][y + 1] == '*':
                    bump_adjacent(grid, x, y)
        print_grid(row[1:-1] for row in grid[1:-1])


solve('minesweeper.txt')


