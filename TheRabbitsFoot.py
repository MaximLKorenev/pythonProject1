def TheRabbitsFoot(s, encode):
    if encode:
        sws = [x for x in s if x != ' ']
        row = int(len(sws) ** 0.5)
        if len(sws) // row == 0:
            column = row
        else:
            column = row + 1
        if len(sws) > row * column:
            row += 1

        m = []
        ind = 0
        for i in range(row):
            a = []
            for j in range(column):
                if ind < len(sws):
                    sym = sws[ind]
                else:
                    sym = ''
                a.append(sym)
                ind += 1
            m.append(a)

        s_encode = ''
        for i in range(column):
            for j in range(row):
                s_encode += m[j][i]
            if i == column - 1:
                break
            s_encode += ' '
        return s_encode
    else:
        list_s = s.split(' ')
        s_decode = ''
        for i in range(len(list_s[-1])):
            for j in range(len(list_s)):
                s_decode += list_s[j][i]
        for i in range(len(list_s)):
            if len(list_s[i]) > len(list_s[-1]):
                s_decode += list_s[i][-1]
            else:
                break
        return s_decode
