with open("inputs/day1.txt") as f:
    q = 50
    res = 0
    for l in f:
        num = int(l[1:])
        if l[0] == "L":
            num *= -1
        q = (q + num) % 100
        if q == 0:
            res += 1

print(res)


with open("inputs/day1.txt") as f:
    q = 50
    res = 0
    for l in f:
        num = int(l[1:])
        for i in range(num):
            if l[0] == "L":
                q = (q - 1) % 100
            else:
                q = (q + 1) % 100

            if q == 0:
                res += 1

print(res)