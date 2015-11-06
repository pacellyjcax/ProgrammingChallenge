while 1:
    try:
        n = int(raw_input())
    except EOFError:
        break

    mat = [['3' for i in range(n)] for j in range(n)]
    for i in range(n):
        mat[i][i] = '1'
        mat[i][-i - 1] = '2'
        print ''.join(mat[i])
