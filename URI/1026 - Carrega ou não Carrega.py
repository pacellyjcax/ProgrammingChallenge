while 1:
    try:
        n = [bin(int(x))[2:] for x in raw_input().split()]
        t1 = len(n[0])
        t2 = len(n[1])
        if t1 > t2:
            n[1] = "".join(["0" for i in xrange((t1-t2))])+n[1]
        elif t1 < t2:
            n[0] = "".join(["0" for i in xrange((t2-t1))])+n[0]
        r = ""
        for i in xrange(len(n[0])):
            if n[0][i] == "1" and n[1][i] == "1":
                r+="0"
            elif n[0][i] == "1" or n[1][i] == "1":
                r+="1"
            else:
                r+="0"
        print int(r,2)
    except:
        break
# TLE even with try-except
'''
while 1:
    n = [bin(int(x))[2:] for x in raw_input().split()]
    a = ["0" for i in xrange(32-len(n[0]))]
    for e in n[0]:
        a.append(e)
    b = ["0" for i in xrange(32-len(n[1]))]
    for e in n[1]:
        b.append(e)
    r = []
    for i in xrange(32):
        if a[i] == "1" and b[i] == "1":
            r.append("0")
        elif a[i] == "1" or b[i] == "1":
            r.append("1")
        else:
            r.append("0")
    print int("".join(r),2) 
'''
# TLE even with try-except
'''
def soma(s,t):
    return str(int(s)+int(t))
while 1:
    try:
        n = [bin(int(x))[2:] for x in raw_input().split()]
        sb = ""
        t1 = len(n[0])
        t2 = len(n[1])
        if t1 > t2:
            n[1] = "".join(["0" for i in xrange((t1-t2))])+n[1]
        elif t1 < t2:
            n[0] = "".join(["0" for i in xrange((t2-t1))])+n[0]
        for i in xrange(len(n[0])):
           sb+=soma(n[0][i],n[1][i])
        sb = sb.replace("2","0")
        print int(sb,2)
    except:
        break
'''
