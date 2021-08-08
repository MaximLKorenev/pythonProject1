def Keymaker(k):
    my_list = ['1' for i in range(k)]
    for i in range(k - 1):
        for j in range(i + 1, k, i + 2):
            if my_list[j] == '1':
                my_list[j] = '0'
            else:
                my_list[j] = '1'
    s = ''.join(my_list)
    return s
