import math
import heapq
import os

def heuristic(a, b, c):
    x1, y1 = c[a]
    x2, y2 = c[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def _find_input_file(a='input.txt'):
    b = []
    if os.path.isabs(a):
        b = [a]
    else:
        b.append(os.path.join(os.getcwd(), a))
        c = os.path.dirname(os.path.abspath(__file__))
        b.append(os.path.join(c, a))
        b.append(os.path.abspath(os.path.join(c, '..', a)))
    for d in b:
        if os.path.exists(d):
            return d, b
    return None, b


def solve():
    d, e = _find_input_file('input.txt')
    if not d:
        print(f"Error: input.txt not found. Tried: {e}")
        return

    with open(d, 'r') as f:
        g = f.read().split()

    h = iter(g)
    i = int(next(h))
    j = {}
    for _ in range(i):
        k = next(h)
        l = float(next(h))
        m = float(next(h))
        j[k] = (l, m)

    n = int(next(h))
    o = {}
    for _ in range(n):
        p = next(h)
        q = next(h)
        r = float(next(h))
        if p not in o:
            o[p] = []
        o[p].append((q, r))

    s = next(h)
    t = next(h)

    u = [(heuristic(s, t, j), s)]
    v = {w: float('inf') for w in j}
    v[s] = 0
    w = {}
    x = set()

    while u:
        _, y = heapq.heappop(u)
        if y == t:
            break
        if y in x:
            continue
        x.add(y)
        for z, aa in o.get(y, []):
            ab = v[y] + aa
            if ab < v.get(z, float('inf')):
                v[z] = ab
                w[z] = y
                ac = ab + heuristic(z, t, j)
                heapq.heappush(u, (ac, z))

    if t not in w and s != t:
        print("No path found.")
    else:
        ad = []
        ae = t
        while ae:
            ad.append(ae)
            ae = w.get(ae)
        ad.reverse()
        print(f"Solution path {' – '.join(ad)}")
        print(f"Solution cost {int(v[t])}")


if __name__ == "__main__":
    solve()