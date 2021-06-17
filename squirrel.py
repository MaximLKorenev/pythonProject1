def squirrel(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return int(str(factorial)[0])
