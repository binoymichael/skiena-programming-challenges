known = "the quick brown fox jumps over the lazy dog"

inputs = ["vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq",
    "xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj",
    "frtjrpgguvj otvxmdxd prm iev prmvx xnmq"]


def mapping_code(inputs, known):
    for sentence in inputs:
        if len(known) == len(sentence):
            mapping = {}
            for a, b in zip(sentence, known):
                if a in mapping:
                    if mapping[a] != b:
                        break
                else:
                    mapping[a] = b
            else:
                return {a: b for a, b in zip(sentence, known)}
    return None

map = mapping_code(inputs, known)

if map:
    for line in inputs:
        print(''.join(map[x] for x in line))
else:
    print("No solution")

