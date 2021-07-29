def TreeOfLife(h, w, n, tree):
    if n == 0:
        return tree
    if n % 2 == 1:
        tree_now = []
        for i in range(h):
            s = ''
            for j in range(w):
                s += '+'
            tree_now.append(s)
        return tree_now

    tree_start = []
    tree_start2 = []
    for i in range(h):
        ts = []
        ts2 = []
        for j in range(w):
            if tree[i][j] == '.':
                ts.append(0)
            else:
                ts.append(1)
            ts2.append(5)
        tree_start.append(ts)
        tree_start2.append(ts2)

    for i in range(n // 2):
        for j in range(h):
            for k in range(w):
                tree_start[j][k] += 2
                if tree_start[j][k] >= 3:
                    tree_start2[j][k] = 0
                    if j > 0:
                        tree_start2[j - 1][k] = 0
                    if j < h - 1:
                        tree_start2[j + 1][k] = 0
                    if k > 0:
                        tree_start2[j][k - 1] = 0
                    if k < w - 1:
                        tree_start2[j][k + 1] = 0

        for j in range(h):
            for k in range(w):
                if tree_start2[j][k] == 0:
                    tree_start[j][k] = tree_start2[j][k]
                tree_start2[j][k] = 5

    tree_now = []
    for i in range(h):
        s = ''
        for j in range(w):
            if tree_start[i][j] == 0:
                s += '.'
            else:
                s += '+'
        tree_now.append(s)
    return tree_now
