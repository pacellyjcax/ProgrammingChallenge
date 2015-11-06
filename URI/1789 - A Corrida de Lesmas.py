while 1:
    try:
        raw_input()
        v = max([int(x) for x in raw_input().split()])
        if v>=20:
            print 3
        elif v>=10:
            print 2
        else:
            print 1
    except:
        break
