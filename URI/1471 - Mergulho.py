while 1:
    try:
        m = [int(x) for x in raw_input().split()]
        n = [int(x) for x in raw_input().split()]
        c = [i+1 for i in xrange(m[0]) if n.count(i+1) == 0]
        if len(c) > 0:
            vf = str(c)
            vf = vf.replace("[","")
            vf = vf.replace("]","")
            vf = vf.replace(",","")
            print vf
        else:
            print '*'
    except:
        break
