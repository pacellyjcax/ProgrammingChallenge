n = int(raw_input())
for i in xrange(n):
    a = 0
    t = 0
    d = raw_input()
    for e in d:       
        if e=='<':
            a+=1
        if e=='>':
            if a>0:
                t+=1
                a-=1
    print t
