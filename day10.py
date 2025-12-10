from itertools import combinations

import numpy as np
from pulp import LpMinimize, LpProblem, lpSum, LpVariable, LpInteger


with open("inputs/day10.txt") as f:
    res = 0
    res2 = 0
    for i, l in enumerate(f):
        print(i)
        segs = l.strip().split()
        lights, *buttons, joltages = segs
        li = np.array([0 if x=="." else 1 for x in lights[1:-1]])
        bs = []
        for but in buttons:
            but2 = [int(x) for x in but[1:-1].split(",")]
            b = np.zeros_like(li)
            b[but2] = 1
            bs.append(b)
        butt = np.array(bs)
        for i in range(1, 666):
            for indices in combinations(range(len(butt)), i):
                lig = np.mod(butt[list(indices)].sum(axis=0), 2)
                if np.all(lig == li):
                    res += i
                    break
            else:
                continue
            break

        jo = [int(x) for x in joltages[1:-1].split(",")]

        model = LpProblem(name="lets-go", sense=LpMinimize)
        variables = [LpVariable(name=f"x{i}", lowBound=0, cat=LpInteger) for i in range(len(buttons))]
        for i, val in enumerate(jo):
            model += lpSum([var for j, var in enumerate(variables) if butt[j,i]==1]) == val

        model += lpSum(variables)
        status = model.solve()
        if status != 1:
            print("something is no yes")

        res2 += sum([x.value() for x in model.variables()])


print(res)
print(res2)
