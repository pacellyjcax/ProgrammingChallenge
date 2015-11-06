while 1:
    n = raw_input()
    if n == "0 0 0 0":
        break
    en = [int(x) for x in n.split()]
    
    if en[0] > en[2]:
        d_x = en[0] - en[2]
    else:
        d_x = en[2] - en[0]

    if en[1] > en[3]:
        d_y = en[1] - en[3]
    else:
        d_y = en[3] - en[1]

    if en[0] == en[2] and en[1] == en[3]:
        print 0
    elif en[0] == en[2] or en[1] == en[3] or d_x == d_y:
        print 1
    else:
        print 2

#versao simplificada
'''
while 1:
    n = raw_input()
    if n == "0 0 0 0":
        break
    en = [int(x) for x in n.split()]

    dx = max(en[0],en[2]) - min(en[0],en[2])
    dy = max(en[1],en[3]) - min(en[1],en[3])

    if en[0] == en[2] and en[1] == en[3]:
        print 0
    elif en[0] == en[2] or en[1] == en[3] or dx == dy:
        print 1
    else:
        print 2
