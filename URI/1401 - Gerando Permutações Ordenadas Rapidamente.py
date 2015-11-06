def perm(s):
    if len(s) <=1:
        yield s
    else:
        for p in perm(s[1:]):
            for i in xrange(len(p)+1):
                yield p[:i] + s[0:1] + p[i:]

n= int(raw_input())
for i in xrange(n):    
    e = [x for x in raw_input()]
    e.sort()
    for p in perm(e):
        print "".join(p)
    if i < n-1:
        print
        
