def josephus(n1,n2):
    if n1 == 1:
        return 0
    return ((josephus(n1 - 1, n2) + n2) % n1)

n = int(raw_input())
for i in xrange(n):
    n1,n2 = map(int,raw_input().split())
    print "Case %d: %d" %(i+1 , josephus(n1,n2) + 1)
 
