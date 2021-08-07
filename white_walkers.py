def white_walkers(village):
    for i in range(len(village) - 4):
        if village[i].isdigit():
            m = i + 1
            x = 0
            while not village[m].isdigit() or m == len(village) - 1:
                if village[m] == '=':
                    x += 1
                m += 1
            if village[m].isdigit() and x == 3 and int(village[i]) + int(village[m]) == 10:
                return True
    return False
