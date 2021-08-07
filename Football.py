def Football(f, n):
    if n == 1:
        return False
    sort_f = f[:]
    sort_f.sort()
    if f == sort_f:
        return False
    a = 0
    b = n - 1
    while a < n - 1:
        if f[a] > f[a + 1]:
            break
        a += 1

    while b > 0:
        if f[b] < f[b - 1]:
            break
        b -= 1

    f1 = f[:]
    f1[a], f1[b] = f1[b], f1[a]
    if f1 == sort_f:
        return True

    f2 = f[a:b]
    f2.sort(reverse=True)
    f3 = f[:a] + f2 + f[b:]

    if f3 == sort_f:
        return True

    return False
