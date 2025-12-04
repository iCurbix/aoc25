import numpy as np
from scipy.signal import convolve2d


kern = [[1,1,1], [1,0,1], [1,1,1]]

with open("inputs/day4.txt") as f:
    grid = []
    for l in f:
        grid.append([1 if x == "@" else 0 for x in l.strip()])
    grid = np.array(grid)
    neighs = convolve2d(grid, kern, "same")
    res = np.logical_and(neighs < 4, grid == 1).sum()

print(res)


with open("inputs/day4.txt") as f:
    grid = []
    res = 0
    for l in f:
        grid.append([1 if x == "@" else 0 for x in l.strip()])
    grid = np.array(grid)
    neighs = convolve2d(grid, kern, "same")
    removable = np.logical_and(neighs < 4, grid == 1)

    while (x := removable.sum()) > 0:
        res += x
        grid[removable] = 0
        neighs = convolve2d(grid, kern, "same")
        removable = np.logical_and(neighs < 4, grid == 1)

    print(res)