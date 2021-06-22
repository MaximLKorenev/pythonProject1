def WordSearch(len_ns, s, subs):
    list_s = s.split()
    list_n = []
    while list_s:
        S = list_s.pop(0)
        if len(S) < len_ns - 1:
            if len(list_s) > 1:
                while len(S + ' ' + list_s[0]) <= len_ns:
                    S += ' ' + list_s.pop(0)
        elif len(S) > len_ns:
            list_s.insert(0, S[len_ns:])
            S = S[:len_ns]
        list_n.append(S)
    my_list = []
    for x in list_n:
        for a in x.split():
            if a == subs:
                my_list.append(1)
                break
        else:
            my_list.append(0)
    return my_list
