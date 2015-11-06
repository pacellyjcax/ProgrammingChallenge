res = []
n = int(raw_input())
tg = 0.0
for i in range(n):
    tg += float(raw_input())
    res.append(len(raw_input().split()))

for i in range(len(res)):
    print "day {0:d}: {1:d} kg".format(i+1,res[i])

print "%.2f kg by day" % (float(sum(res))/n)
print "R$ %.2f by day" % (tg/n)
