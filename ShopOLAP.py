def ShopOLAP(n, items):
    list_items = []
    for item in items:
        list_items.append(item.split())

    lwr = []
    for i in range(n):
        numb = 0
        if list_items[i][0] not in lwr:
            for j in range(n):
                if list_items[i][0] == list_items[j][0]:
                    numb += int(list_items[j][1])
            lwr.append(list_items[i][0])
            lwr.append(numb)

    flag = True
    while flag:
        flag = False
        for i in range(1, len(lwr) - 2, 2):
            if lwr[i] < lwr[i + 2]:
                lwr[i - 1], lwr[i], lwr[i + 1], lwr[i + 2] = lwr[i + 1], lwr[i + 2], lwr[i - 1], lwr[i]
                flag = True
            elif lwr[i] == lwr[i + 2]:
                if lwr[i - 1] > lwr[i + 1]:
                    lwr[i - 1], lwr[i + 1] = lwr[i + 1], lwr[i - 1]
                    flag = True

    new_list = []
    for i in range(0, len(lwr), 2):
        a = '{0} {1}'.format(lwr[i], lwr[i + 1])
        new_list.append(a)
    return new_list
