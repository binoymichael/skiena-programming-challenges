DICTIONARY = """booster
rooster
roaster
coasted
roasted
coastal
postal"""

dictionary = set(DICTIONARY.splitlines())

def possibilites(source, destination):
    result = []
    for index, value in enumerate(zip(source, destination)):
        if value[0] != value[1]:
            possibility = list(source)
            possibility[index] = destination[index]
            if ''.join(possibility) in dictionary:
                result.append(possibility)
    return result

def solve(start, end, path=[]):
    queue = [[start]]
    while queue:
        path = queue.pop()
        node = path[-1]
        if node == end:
            return path
        for p in possibilites(node, end):
            new_path = list(path)
            new_path.append(p)
            queue.append(new_path)
    return False

r = solve(list('booster'), list('roasted'))
print(r)
