def PatternUnlock(N, hits):
    ln = 0
    for i in range(N - 1):
        a = hits[i]
        b = hits[i + 1]
        if (a == 1 or a == 3) and (b == 5 or b == 8):
            ln += 2 ** 0.5
        elif a == 2 and (b == 6 or b == 9 or b == 7 or b == 4):
            ln += 2 ** 0.5
        elif (a == 4 or a == 7 or a == 6 or a == 9) and b == 2:
            ln += 2 ** 0.5
        elif (a == 5 or a == 8) and (b == 1 or b == 3):
            ln += 2 ** 0.5
        else:
            ln += 1
    ln_str_with_0 = str(int(round(ln, 5) * 100000))
    ln_str_list = [x for x in ln_str_with_0 if x != '0']
    ln_str = ''
    for x in ln_str_list:
        ln_str += x
    return ln_str
