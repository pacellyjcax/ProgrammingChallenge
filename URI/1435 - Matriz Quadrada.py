while 1:
    n = int(raw_input())
    
    if n == 0:
        break

    mat = [[1 for i in range(n)] for j in range(n)]
    
    for k in range(1, (n - 1) / 2 + 1):
        for i in range(k, n - k):
            for j in range(k, n - k):
                mat[i][j] += 1

    for i in range(n):
        l = ['%3d' % n for n in mat[i]]
        print " ".join(l)
    print
