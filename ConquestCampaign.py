def ConquestCampaign(N, M, L, battalion):
    a = []
    for i in range(N):
        b = []
        for j in range(M):
            b.append(0)
        a.append(b)

    start = 0
    for _ in range(L):
        x = battalion[start] - 1
        y = battalion[start + 1] - 1
        a[x][y] = 1
        start += 2

    days = 1
    while [1 for i in a if 0 in i]:
        b = [x[:] for x in a]
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 1:
                    if i - 1 >= 0 and a[i - 1][j] == 0:
                        b[i - 1][j] = 1
                    if i + 1 < len(a) and a[i + 1][j] == 0:
                        b[i + 1][j] = 1
                    if j - 1 >= 0 and a[i][j - 1] == 0:
                        b[i][j - 1] = 1
                    if j + 1 < len(a[i]) and a[i][j + 1] == 0:
                        b[i][j + 1] = 1
        a = [x[:] for x in b]
        days += 1

    return days
