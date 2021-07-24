def BiggerGreater(inp):
    a = []
    a.extend(inp)
    b = a[:]
    n = len(a) - 1
    flag1 = True
    for i in range(n):
        if flag1:
            for j in range(n - i):
                if a[-1 - i] > a[-2 - j - i]:
                    a[-1 - i], a[-2 - j - i] = a[-2 - j - i], a[-1 - i]
                    flag1 = False
                    x = -2 - j - i
                    break
    if a == b:
        return ''
    c = a[: len(a) + x + 1]
    d = a[len(a) + x + 1:]
    d.sort()
    bigger = ''.join(c + d)
    return bigger
