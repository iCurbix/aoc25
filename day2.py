with open("inputs/day2.txt") as f:
    res = 0
    for r in f.read().split(","):
        a, b = r.split("-")
        aa, bb = int(a), int(b)
        x = int(a[:len(a) // 2 + len(a) % 2])
        if x > 9:
            x = x // 10
        while ...:
            xx = int(str(x) * 2)
            if xx > bb:
                break
            if xx >= aa:
                res += xx
            x += 1

print(res)


with open("inputs/day2.txt") as f:
    res = 0
    for r in f.read().split(","):
        a, b = r.split("-")
        aa, bb = int(a), int(b)
        found = set()
        for x in range(1, int(b[:len(b) // 2 + len(b) % 2] or 0) + 1):
            for i in range(2, 666):
                xx = int(str(x) * i)
                if xx > bb:
                    break
                if xx >= aa and xx not in found:
                    found.add(xx)
                    res += xx

print(res)