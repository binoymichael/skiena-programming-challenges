from collections import defaultdict
from collections import OrderedDict
from collections import ChainMap

DATA = """7
and
dick
jane
puff
spot
her
yertle
bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn
xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd
"""


def decipher(sentence):
    words = defaultdict(set)
    for word in sentence.split(' '):
        words[len(word)].add(word)
    words = sorted(words.items(), key=lambda x: len(x[1]))
    words = [s for x, y in words for s in y]
    if solve(words):
        c = ChainMap(*mapping_stack)
        for char in sentence:
            if char in c:
                print(c[char], end='')
            else:
                print(' ', end='')
        print()
    else:
        print('no output')


def is_valid_map(z):
    chain_map = ChainMap({}, *mapping_stack)
    for x in z:
        if x in chain_map:
            if chain_map[x] != z[x]:
                return False
        else:
            chain_map[x] = z[x]
    else:
        return True


def solve(words):
    head, *tail = words
    possible_matches = dictionary[len(head)]
    for p in possible_matches:
        m = {x: y for x, y in zip(head, p)}
        if is_valid_map(m):
            mapping_stack.append(m)
            if not tail:
                return True
            if solve(tail):
                return True
            else:
                mapping_stack.pop()
    else:
        return False


lines = iter(DATA.split("\n"))

dictionary_length = int(next(lines));
dictionary = defaultdict(list)
for x in range(dictionary_length):
    word = next(lines)
    dictionary[len(word)].append(word)
dictionary = OrderedDict(sorted(dictionary.items(), key=lambda x: len(x[1])))

sentence = next(lines)
mapping_stack = [{}]
decipher(sentence)
