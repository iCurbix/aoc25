import functools


def dfs(cur: str, g: dict[str, list[str]]) -> int:
    r = 0
    for des in g[cur]:
        if des == "out":
            r += 1
            continue
        r += dfs(des, g)
    return r


@functools.lru_cache(maxsize=None)
def dfs2(cur: str, dac: bool, fft: bool) -> int:
    r = 0
    dac2 = dac or cur == "dac"
    fft2 = fft or cur == "fft"
    for des in g[cur]:
        if des == "out":
            if dac and fft:
                r += 1
            continue
        r += dfs2(des, dac2, fft2)
    return r


with open("inputs/day11.txt") as f:
    res = 0
    g = {}
    for l in f:
        a, dests = l.split(":")
        dests = dests.strip().split()
        g[a] = dests

print(dfs("you", g))
print(dfs2("svr", False, False))

