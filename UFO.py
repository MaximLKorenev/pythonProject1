def UFO(N, data, octal):
    if octal:
        coef = 8
    else:
        coef = 16
    data_4_earth = []
    for i in range(N):
        a = str(data[i])
        b = len(a) - 1
        c = 0
        for x in a:
            c += int(x) * coef ** b
            b -= 1
        data_4_earth.append(c)
    return data_4_earth
