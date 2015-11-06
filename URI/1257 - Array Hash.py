def val(s,v,vs):
    return (ord(s)-65)+v+vs

n = int(raw_input())
for i in xrange(n):
    st = 0
    m = int(raw_input())
    for j in xrange(m):
        en = raw_input()
        st += sum([val(en[k],j,k) for k in xrange(len(en))])
    print st
