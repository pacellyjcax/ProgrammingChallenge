t1 = raw_input().split()
t2 = raw_input().split()
r = "Y"
for i in xrange(5):
    if t1[i] == t2[i]:
        r = "N"
        break
print r
    
