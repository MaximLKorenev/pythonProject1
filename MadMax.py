def MadMax(N, Tele):
    if N == 1:
        return Tele
    if N <= 5:
        Tele[N // 2], Tele[N - 1] = Tele[N - 1], Tele[N // 2]
        return Tele
    n = N // 2
    for _ in range(n - 1):
        Tele[n], Tele[N - 1] = Tele[N - 1], Tele[n]
        n += 1
        N -= 1
    return Tele
