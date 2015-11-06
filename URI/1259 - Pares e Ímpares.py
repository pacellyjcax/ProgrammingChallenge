res = {"p":[],"i":[]}
n = int(raw_input())
for i in range(n):    
    v = int(raw_input())
    if v%2 == 0:
        res["p"].append(v)
    else:
        res["i"].append(v)

res["p"].sort()
res["i"].sort(reverse=True)
for e in res["p"]:
    print e
for e in res["i"]:
    print e
