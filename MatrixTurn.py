def MatrixTurn(Matrix, M, N, T):
    Matrix_c = []
    for i in range(M):
        line = []
        for j in range(N):
            line.append(Matrix[i][j])
        Matrix_c.append(line)

    if M <= N:
        m = M // 2
    else:
        m = N // 2

    for _ in range(T):
        for i in range(m):
            sm = 0 + i
            sn = 0 + i
            x = M - 2 * i
            y = N - 2 * i
            n = (x + y - 2) * 2
            start = Matrix_c[sm][sn]
            for j in range(n):
                if j < x - 1:
                    Matrix_c[sm][sn] = Matrix_c[sm + 1][sn]
                    sm += 1
                elif j < x + y - 2:
                    Matrix_c[sm][sn] = Matrix_c[sm][sn + 1]
                    sn += 1
                elif j < 2 * x + y - 3:
                    Matrix_c[sm][sn] = Matrix_c[sm - 1][sn]
                    sm -= 1
                elif j < n - 1:
                    Matrix_c[sm][sn] = Matrix_c[sm][sn - 1]
                    sn -= 1
                else:
                    Matrix_c[sm][sn] = start

    for i in range(M):
        s = ''
        for j in range(N):
            s += Matrix_c[i][j]
        Matrix[i] = s
