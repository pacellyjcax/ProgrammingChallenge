n = int(raw_input())
for i in xrange(n):
    int(raw_input())
    m = [int(x) for x in raw_input().split()]
    o = raw_input()
    t = 0
    for j in xrange(len(o)):
        if m[j] > 2 and o[j] == "J":
            t+=1
        elif m[j] <= 2 and o[j] == "S":
            t+=1
    print t
