while 1:
    n= int(raw_input())
    if n == 0:
        break
    e = [int(x) for x in raw_input().split()]
    s = int(raw_input())
    while not s == e[s-1]:
        s = e[s-1]
    print s
