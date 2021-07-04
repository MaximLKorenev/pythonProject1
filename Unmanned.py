def Unmanned(L, N, track):
    start = 0
    time = 0
    for i in range(N):
        time += track[i][0] - start
        start = track[i][0]
        rs = 0
        re = gs = track[i][1]
        ge = gs + track[i][2]
        while ge < time:
            rs += ge
            re += ge
            gs += ge
            ge += ge
        if time < re:
            time = re
    time += L - start
    return time
