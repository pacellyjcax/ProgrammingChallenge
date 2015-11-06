def rec(n1,n2):
    if n1 == 1:
        return 0
    return ((rec(n1 - 1, n2) + n2) % n1)

while 1:
    n = int(raw_input())
    if n == 0:
        break
    i = 1
    while 1:
        res = rec(n - 1, i) + 2
        if res == 13:
            print i
            break
