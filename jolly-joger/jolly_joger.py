DATA="""4 1 4 2 3
5 1 4 2 -1 6"""


def process(input):
    length = len(input)
    bitmap = list(range(length - 1))
    for i, x in enumerate(input[:-1]):
        diff = abs(int(x) - int(input[i + 1]))
        if diff < length:
            bitmap[diff] = 0
    result = "Not Jolly" if any(x != 0 for x in bitmap) else "Jolly"
    print(result)


lines = iter(DATA.split("\n"))

for line in lines:
    process(line.split())



