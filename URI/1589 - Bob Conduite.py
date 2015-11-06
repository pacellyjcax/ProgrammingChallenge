res = []
for i in range(int(raw_input())):
    res.append(sum([int(x) for x in raw_input().split()]))
 
for e in res:
    print e
