
res = []

while 1:
    n = int(raw_input())
    if n == 0:
        break
    e = [int(x) for x in raw_input().split()]
    res.append((e.count(0),e.count(1)))

for e in res:
    print "Mary won {0:d} times and John won {1:d} times".format(e[0],e[1])
