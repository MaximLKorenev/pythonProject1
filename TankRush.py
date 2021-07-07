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
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            if m1[i][j] == m2[0][0]:
                flag = True
                for k in range(h2):
                    if not flag:
                        break
                    for m in range(w2):
                        if m1[i + k][j + m] != m2[k][m]:
                            flag = False
                            break
                        elif (m1[i + k][j + m] == m2[k][m]
                              and k == h2 - 1 and m == w2 - 1):
                            return True
    return False
