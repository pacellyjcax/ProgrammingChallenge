res = []
n = int(raw_input())
for i in range(n):
    e = [int(x) for x in raw_input().split()]
    res.append(e[(e[0]/2)+1])

for i in range(n):
    print "Case {0:d}: {1:d}".format(i+1,res[i])
