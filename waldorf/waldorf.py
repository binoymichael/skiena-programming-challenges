GRID="""abcDEFGhigg
hEbkWalDork
FtyAwaldORm
FtsimrLqsrc
byoArBeDeyv
Klcbqwikomk
strEBGadhrb
yUiqlxcnBjf
"""

lines = iter(GRID.splitlines())
rows = 8
cols = 11
space = [[' ' for y in range(cols + 2)] for x in range(rows + 2)]
for index, line in enumerate(lines, 1):
    space[index][1:-1] = list(line)


def search_space_for(solution):
    if not solution:
        return range(1, rows + 1), range(1, cols + 1)
    if len(solution) == 1:
        i, j = solution[0]
        return range(i - 1, i + 2), range(j - 1, j + 2)
    else:
        pen, last = solution[-2:]
        x_delta, y_delta = (last[0] - pen[0], last[1] - pen[1])
        next_x = last[0] + x_delta
        next_y = last[1] + y_delta
        return range(next_x, next_x + 1), range(next_y, next_y + 1)

def solve(search, path = []):
    if not search:
        return path
    head, *tail = search
    range_x, range_y = search_space_for(path)
    for i in range_x:
        for j in range_y:
            if space[i][j].lower() == head.lower():
                solution = solve(tail, path + [(i, j)])
                if solution:
                    return solution
    return False

for word in ['Waldorf', 'Bambi', 'Betty', 'Dagbert']:
    print(solve(word, []))

