def white_walkers(village):
    a = 0
    b = 0
    i = 0
    while i < len(village) - 2:
        if village[i].isdigit():
            m = i + 1
            x = 0
            while m != len(village) - 1:
                if village[m].isdigit():
                    break
                elif village[m] == '=':
                    x += 1
                m += 1
            if village[m].isdigit() and int(village[i]) + int(village[m]) == 10:
                b += 1
                if x == 3:
                    a += 1
                i = m - 1
        i += 1

    if a == b and a != 0:
        return True
    return False
