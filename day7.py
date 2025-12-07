from collections import defaultdict

with open("inputs/day7.txt") as f:
    res = 0
    beams = {next(f).index("S")}
    for l in f:
        new_beams = set()
        for bx in beams:
            if l[bx] == "^":
                res += 1
                new_beams.update({bx - 1, bx + 1})
            else:
                new_beams.add(bx)
        beams = new_beams

print(res)


with open("inputs/day7.txt") as f:
    beams = defaultdict(int)
    beams[next(f).index("S")] += 1
    for l in f:
        new_beams = defaultdict(int)
        for bx, x in beams.items():
            if l[bx] == "^":
                new_beams[bx - 1] += x
                new_beams[bx + 1] += x
            else:
                new_beams[bx] += x
        beams = new_beams

print(sum(beams.values()))