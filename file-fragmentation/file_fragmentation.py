from collections import defaultdict
DATA="""011
01110
0111
0111
111
10111"""


def is_valid_piece(contender, pattern):
    if not pattern:
        return True
    else:
        a, b = contender
        return a[1] + b[1] == pattern


def possible_mappings_for(head):
    piece_length = len(head[1])
    possible_pieces = mapping[file_length - piece_length]
    return [(head, x) for x in possible_pieces] + [(x, head) for x in possible_pieces]


def solve(lines, correct_combo = ""):
    if not lines:
        return correct_combo

    head, *tail = lines
    pm = possible_mappings_for(head)
    for combined_piece in pm:
        first, second = combined_piece
        if is_valid_piece(combined_piece, correct_combo):
           pruned = [i for i in tail if i != second]
           result = solve(pruned, first[1] + second[1])
           if result:
               return result
    return False


lines = list(enumerate(DATA.splitlines()))
file_length = sum(len(l[1]) for l in lines) // len(lines) * 2

mapping = defaultdict(list)
for index, value in lines:
    mapping[len(value)].append((index, value))

result = solve(lines, "")
print(result)

