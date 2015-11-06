res = []
while 1:
    e = raw_input()
    if e == "0 0":
        break
    
    res.append(sum([int(x)for x in e.split()]))

for e in res:
    print e
