def TankRush(h1, w1, s1, h2, w2, s2):
    l1 = s1.split(' ')
    l2 = s2.split(' ')
    m1 = []
    m2 = []
    for i in range(h1):
        a = []
        for j in range(w1):
            a.append(l1[i][j])
        m1.append(a)
    for i in range(h2):
        b = []
        for j in range(w2):
            b.append(l2[i][j])
        m2.append(b)
    find = 0
    for i in range(h2):
        if find < i:
            return False
        for j in range(h1):
            if find > i:
                break
            for k in range(w1 - w2 + 1):
                if find > i:
                    break
                for m in range(w2):
                    if m2[i][m] != m1[j][k + m]:
                        break
                    elif m2[i][m] == m1[j][k + m] and m == w2 - 1:
                        find += 1
                        break
    if find == h2:
        return True
    else:
        return False
