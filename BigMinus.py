def BigMinus(s1, s2):
    if int(s1) < int(s2):
        s1, s2 = s2, s1
    elif s1 == s2:
        return '0'
    s1 = list(s1)
    s2 = list(s2)
    data = []
    for i in range(len(s2)):
        n = -1 - i
        x = int(s1[n]) - int(s2[n])
        if x >= 0:
            data.insert(0, str(x))
        else:
            data.insert(0, str(x + 10))
            s1[n - 1] = str(int(s1[n - 1]) - 1)

    if len(s1) > len(s2):
        data = s1[:len(s1) - len(s2)] + data
    n = 0
    for x in data:
        if x == '0':
            n += 1
        else:
            break
    data = data[n:]
    data = ''.join(data)
    return data
