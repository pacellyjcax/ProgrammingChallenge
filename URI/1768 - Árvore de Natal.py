def imparv(n):
    v = 1
    e = n/2
    while v <=n:
        print "".join([" " for i in range(e)])+"".join(["*" for i in range(v)])
        e -= 1
        v += 2
    print "".join([" " for i in range(n/2)])+"*"
    print "".join([" " for i in range((n/2)-1)])+"***"


while 1:
    try:
        e = int(raw_input())
        imparv(e)
        print
    except:
        break

