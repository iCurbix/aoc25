def do(l: str, ps: list[int]) -> bool:
    q, cs = l.split(":")
    ass, bss = q.split("x")
    a, b = int(ass), int(bss)
    s = 0
    for i, c in enumerate(cs.split()):
        s += ps[i] * int(c)
    if a*b >= s:
        return True
    return False

with open("inputs/day12.txt") as f:
    res = 0
    p = []
    for l in f:
        if "x" in l:
            break
        if ":" in l:
            q = 0
            for ll in f:
                if ll == "\n":
                    p.append(q)
                    break
                q += ll.count("#")
    if do(l, p):
        res += 1
    for l in f:
        if do(l, p):
            res += 1

print(res)
