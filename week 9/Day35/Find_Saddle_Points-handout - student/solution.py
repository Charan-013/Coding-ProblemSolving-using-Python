def saddle_point(m1):
    a = []
    b = []
    
    new = [list(row) for row in zip(*m1)]

    for c, ch in zip(m1, new):
        min_r, max_col = min(c), max(ch)
        a.append(min_r)
        b.append(max_col)

    for i, ch in enumerate(a):
        for j, c in enumerate(b):
            if ch == c:
                return [(i, j)]


m1 = eval(input())

print(saddle_point(m1))
