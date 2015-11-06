
res = []
n = int(raw_input())
for i in xrange(n):
    int(raw_input())    
    e = raw_input()
    en = [int(x) for x in e.split()]    
    if len(en)>1:
        t = 1
        s = "".join([str(x) for x in en])
        vm = max(en)
        for i in xrange(len(en),1,-1):
            if s.count("".join([str(vm) for x in xrange(i)]))==1:
                res.append(i)
                break
    else:
        res.append(1)
    
for i in xrange(len(res)):
    print "Caso #{0:d}: {1:d}".format((i+1),res[i])

#time limit
'''
res = []
n = int(raw_input())
for i in range(n):
    int(raw_input())
    en = [int(x) for x in raw_input().split()]
    if len(en)>1:
        t = 1
        s = True
        lt = []
        vm =max(en)
        for i in range(1,len(en)):
            if en[i] == en[i-1]:
                if s:
                    t+=1
                    s = True
                else:
                    s = True
            else:
                t = 1
                s = False
            lt.append(t)
        res.append(max(lt))
    else:
        res.append(1)
    
for i in range(len(res)):
    print "Caso #{0:d}: {1:d}".format((i+1),res[i])
'''
