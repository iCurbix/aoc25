with open("inputs/day3.txt") as f:
    res = 0
    for l in f:
        l = l.strip()
        if b := l.split(a := max(l), 1)[1]:
            res += int(a+max(b))
            continue
        a2 = max(l.replace(a, ""))
        res += int(a2 + max(l.split(a2, 1)[1]))

print(res)


def jolt(l: str, n: int) -> str:
    if not l:
        return ""
    if n == 1:
        return max(l)
    ll = l
    while ll:
        q = max(ll)
        ll, rr = l.split(q, 1)
        if qq := jolt(rr, n-1):
            return q + qq

    return ""


with open("inputs/day3.txt") as f:
    res = 0
    for l in f:
        l = l.strip()
        print(int(jolt(l, 12)))
        res += int(jolt(l, 12))

print(res)
