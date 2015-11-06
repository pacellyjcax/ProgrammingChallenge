while 1:
    en = [int(x) for x in raw_input().split()]
    if sum(en) == 0:
        break
    to = [0 for i in xrange(en[1])]
    te = [1 for i in xrange(4)]
    for i in xrange(en[0]):
        a = [int(x) for x in raw_input().split()]
        if len(a) == sum(a) and not te[0] == 0:
            te[0] = 0
        elif sum(a) == 0 and not te[3] == 0:
            te[3] = 0
        for j in xrange(en[1]):
            to[j]+=a[j]
    for e in to:
        if e == en[0] and not te[2] == 0:
            te[2] = 0
        elif e == 0 and not te[1] == 0:
            te[1] = 0
    print sum(te)
'''
while 1:
    en = [int(x) for x in raw_input().split()]
    if sum(en) == 0:
        break
    to = [0 for i in xrange(en[1])]
    te = [False for i in xrange(4)]
    for i in xrange(en[0]):
        a = [int(x) for x in raw_input().split()]
        if len(a) == sum(a) and not te[0]:
            te[0] = True
        elif sum(a) == 0 and not te[3]:
            te[3] = True
        for j in xrange(en[1]):
            to[j]+=a[j]
    t = 4
    for e in to:
        if e == en[0]:
            te[2] = True
        elif e == 0:
            te[1] = True
    if te[0]:
        t-=1
    if te[1]:
        t-=1
    if te[2]:
        t-=1
    if te[3]:
        t-=1
    print t
'''
