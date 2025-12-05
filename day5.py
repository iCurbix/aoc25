with open("inputs/day5.txt") as f:
    res = 0
    ranges = []
    for l in f:
        if l == "\n":
            break
        a, b = l.split("-")
        ranges.append((int(a), int(b)))

    for l in f:
        q = int(l)
        for r in ranges:
            if r[0] <= q <= r[1]:
                res += 1
                break

print(res)


with open("inputs/day5.txt") as f:
    ranges = []
    for l in f:
        if l == "\n":
            break
        a, b = l.split("-")
        aa, bb = int(a), int(b)
        cur_ranges = [(aa, bb)]
        for r in ranges:
            new_cur_ranges = []
            for cr in cur_ranges:
                if r[0] <= cr[0] <= r[1] and r[0] <= cr[1] <= r[1]:
                    break
                if cr[0] < r[0] <= cr[1]:
                    new_cur_ranges.append((cr[0], r[0]-1))
                if cr[0] <= r[1] < cr[1]:
                    new_cur_ranges.append((r[1]+1, cr[1]))
                if r[0] > cr[1] or r[1] < cr[0]:
                    new_cur_ranges.append(cr)

            cur_ranges = new_cur_ranges

        ranges += cur_ranges

print(sum(r[1] - r[0] + 1 for r in ranges))
