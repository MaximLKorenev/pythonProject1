def Unmanned(L, N, track):
    start = 0
    time = 0
    for i in range(N):
        if L <= track[i][0]:
            break
        time += track[i][0] - start
        start = track[i][0]
        rs = 0
        re = gs = track[i][1]
        cycle = ge = gs + track[i][2]
        while ge < time:
            rs += cycle
            re += cycle
            gs += cycle
            ge += cycle
        if time < re:
            time = re
    time += L - start
    return time
