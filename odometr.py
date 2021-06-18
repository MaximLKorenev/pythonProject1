def odometr(oksana):
    oksana = list(oksana)
    distance = oksana[0] * oksana[1]
    for i in range(2, len(oksana), 2):
        distance += oksana[i] * (oksana[i + 1] - oksana[i - 1])
    return distance
