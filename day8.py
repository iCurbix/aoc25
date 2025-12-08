
def dist2(x1, y1, z1, x2, y2, z2):
    return (x1-x2) ** 2 + (y1-y2) ** 2 + (z1-z2) ** 2


with open("inputs/day8.txt") as f:
    boxes = []
    dists = []
    for i, l in enumerate(f):
        x, y, z = [int(x) for x in l.split(",")]
        for i2, (x2, y2, z2) in enumerate(boxes):
            d2 = dist2(x, y, z, x2, y2, z2)
            dists.append((i, i2, d2))
        boxes.append((x, y, z))

dists.sort(key=lambda x: x[2])
circs = []
for ai, bi, d2 in dists[:1000]:
    new_circs = []
    ac = None
    bc = None
    for c in circs:
        if ai in c:
            ac = c
        if bi in c:
            bc = c
        if ai not in c and bi not in c:
            new_circs.append(c)
    if ac and bc and ac == bc:
        new_circs.append(ac)
    elif ac and bc:
        new_circs.append(ac + bc)
    elif ac:
        new_circs.append(ac + [bi])
    elif bc:
        new_circs.append(bc + [ai])
    else:
        new_circs.append([ai, bi])
    circs = new_circs

circs.sort(key=lambda x: -len(x))

print(len(circs[0]) * len(circs[1]) * len(circs[2]))

for ai, bi, d2 in dists[1000:]:
    new_circs = []
    ac = None
    bc = None
    for c in circs:
        if ai in c:
            ac = c
        if bi in c:
            bc = c
        if ai not in c and bi not in c:
            new_circs.append(c)
    if ac and bc and ac == bc:
        new_circs.append(ac)
    elif ac and bc:
        new_circs.append(ac + bc)
    elif ac:
        new_circs.append(ac + [bi])
    elif bc:
        new_circs.append(bc + [ai])
    else:
        new_circs.append([ai, bi])
    circs = new_circs

    if len(circs) == 1 and len(circs[0]) == len(boxes):
        print(boxes[ai][0] * boxes[bi][0])
        break