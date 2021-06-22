def SumOfThe(N, data):
    sum = 0
    for i in range(N):
        sum += data[i]
    sum //= 2
    return sum
