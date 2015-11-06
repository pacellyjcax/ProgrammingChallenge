while 1:
    a = raw_input().split("/")
    if a[0] == "*":
        break
    v = {"W":1.0,"H":0.50,"Q":0.25,"E":0.125,"S":0.0625,"T":0.03125,"X":0.015625}
    t = 0
    for e in a:
        b = [v[x] for x in e]
        if sum(b) == 1.0:
            t += 1
    print t
