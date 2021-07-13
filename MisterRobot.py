def MisterRobot(n, data):
    sort_data = data[:]
    sort_data.sort()
    flag = True
    while flag:
        flag = False
        for i in range(n - 2):
            if (data[i + 1] > data[i] > data[i + 2] or
                    data[i] > data[i + 1] and data[i + 1] < data[i + 2]):
                data[i], data[i + 1], data[i + 2] = data[i + 1], data[i + 2], data[i]
                flag = True
    if data == sort_data:
        return True
    else:
        return False
