import numpy as np


with open("inputs/day6.txt") as f:
    inpt = []
    for l in f:
        inpt.append(l.split())

    arr = np.array([[int(x) for x in row] for row in inpt[:-1]])

    s = np.sum(arr, axis=0)[[True if op == "+" else False for op in inpt[-1]]].sum()
    p = np.prod(arr, axis=0)[[True if op == "*" else False for op in inpt[-1]]].sum()

print(s+p)


with open("inputs/day6.txt") as f:
    res = 0
    inpt = []
    for l in f:
        inpt.append(l[:-1])

    arr = np.array([[x for x in row] for row in inpt[:-1]])
    split = np.hsplit(arr, np.where(np.all(arr == ' ', axis=0))[0])
    split2 = [np.delete(ss, 0, 1) for ss in split[1:]]
    split2 = [split[0]] + split2
    for ss, op in zip(split2, inpt[-1].split()):
        nums = np.apply_along_axis(lambda x: int("".join(x)), 0, ss)
        if op == "+":
            res += np.sum(nums)
        else:
            res += np.prod(nums)

print(res)