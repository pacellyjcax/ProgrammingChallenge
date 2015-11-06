while 1:
    n = int(raw_input())

    if n == 0:
        break

    mat = [[1 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] += abs(j - i)

    for i in range(n):
        l = ['%3d' % n for n in mat[i]]
        print ' '.join(l)
    print
