DICTIONARY = """booster
rooster
roaster
coasted
roasted
coastal
postal"""

dictionary = set(DICTIONARY.splitlines())
print(dictionary)


def possibilites(source, destination):
    result = []
    for index, value in enumerate(zip(source, destination)):
        if value[0] != value[1]:
            possibility = list(source)
            possibility[index] = destination[index]
            if ''.join(possibility) in dictionary:
                result.append(possibility)
    return result


def solve(source, destination, path=[]):
    if source == destination:
        return path
    possible = possibilites(source, destination)
    for p in possible:
        result = solve(p, destination, path + [p])
        if result:
            return result
    return False


r = solve(list('booster'), list('roasted'), path=[])
print(r)
r = solve(list('coastal'), list('postal'), path=[])
print(r)

