while 1:
    a, c = map(int, raw_input().split())
    if a == c == 0:
        break
    alt = map(int, raw_input().split())
    altTemp = a
    t = 0
    for h in alt:
        if h < altTemp:
            t += altTemp - h
        altTemp = h
    print t
