import re

def process(filename):
    def replace_dot_with_zeroes(c): return 0 if c == '.' else c
    f = open(filename, 'r')
    while True:
        line = f.readline().strip()
        if line == '0 0': break
        grid_size_regex = r"(\d+) (\d+)"
        match = re.search(grid_size_regex, line)
        if match:
            rows = int(match.group(1))
            cols = int(match.group(2))
            grid = []
            for _ in range(rows):
                l = f.readline().strip()
                grid.append(list(map(replace_dot_with_zeroes, list(l))))
            solve_grid(grid, rows, cols)
    f.close()

def solve_grid(grid, rows, cols):
    print(rows, cols)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '*':
                bump_adjacent(grid, i, j, rows, cols)
    print_grid(grid)


def print_grid(grid):
    for row in grid:
        print("".join(str(v) for v in row))
    print

def bump_adjacent(grid, i, j, rows, cols):
    x1 = i if i - 1 < 0 else i - 1
    y1 = j if j - 1 < 0 else j - 1
    x2 = i if i + 1 >= rows else i + 1
    y2 = j if j + 1 >= cols else j + 1
    for m in range(x1, x2 + 1):
        for n in range(y1, y2 + 1):
            if grid[m][n] != '*': grid[m][n] += 1


process('minesweeper.txt')
