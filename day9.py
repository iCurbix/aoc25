from itertools import pairwise


def area(x1, y1, x2, y2):
    return (abs(x1-x2)+1) * (abs(y1-y2)+1)


with open("inputs/day9.txt") as f:
    cords = []
    maxi = 0
    for l in f:
        x, y = [int(x) for x in l.split(",")]
        for x2, y2 in cords:
            maxi = max(maxi, area(x, y, x2, y2))
        cords.append((x, y))

print(maxi)

# +1 |
#    |__ -1
#   0

inside = ["r"]
for i, (x, y) in enumerate(cords[2:]):
    match inside[-1]:
        case "r":
            if y > cords[i-2][1]:
                if x > cords[i-1][0]:
                    inside.append("d")
                else:
                    inside.append("u")
            else:
                if x > cords[i - 1][0]:
                    inside.append("u")
                else:
                    inside.append("d")
        case "l":
            if y > cords[i - 2][1]:
                if x > cords[i - 1][0]:
                    inside.append("u")
                else:
                    inside.append("d")
            else:
                if x > cords[i - 1][0]:
                    inside.append("d")
                else:
                    inside.append("u")
        case "u":
            if x > cords[i - 2][0]:
                if y > cords[i - 1][1]:
                    inside.append("l")
                else:
                    inside.append("r")
            else:
                if y > cords[i - 1][1]:
                    inside.append("r")
                else:
                    inside.append("l")
        # im loosing my mind
        case "d":
            if x > cords[i - 2][0]:
                if y > cords[i - 1][1]:
                    inside.append("r")
                else:
                    inside.append("l")
            else:
                if y > cords[i - 1][1]:
                    inside.append("l")
                else:
                    inside.append("r")

inside.append("u")


maxi = 0
for i, (x, y) in enumerate(cords):
    for x2, y2 in cords[i+1:]:
        # match inside[i]:
        #     case "u":
        #         if y2 < y:
        #             continue
        #     case "d":
        #         if y2 > y:
        #             continue
        #     case "l":
        #         if x2 > x:
        #             continue
        #     case "r":
        #         if x2 < x:
        #             continue
        for (x3, y3), (x4, y4) in pairwise(cords + [cords[-1]]):
            if not(min(x3, x4) >= max(x, x2) or max(x3, x4) <= min(x, x2) or min(y3, y4) >= max(y, y2) or max(y3, y4) <= min(y, y2)):
                break
        else:
            maxi = max(maxi, area(x, y, x2, y2))

print(maxi)
