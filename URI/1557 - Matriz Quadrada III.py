while 1:
    n = int(raw_input())

    if n == 0:
        break

    mat = [[1 for i in range(n)] for j in range(n)]
    for j in range(1, n):
        mat[0][j] = mat[0][j - 1] * 2

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                mat[i][j] = mat[i - 1][j] * 2
            else:
                mat[i][j] = mat[i][j - 1] * 2
   
    mx = len(str(mat[-1][-1]))
    for i in range(n):
        l = ['%*d' % (mx, n) for n in mat[i]]
        print ' '.join(l)
    print
