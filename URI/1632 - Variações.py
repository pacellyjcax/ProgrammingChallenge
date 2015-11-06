
res = []
for i in range(int(raw_input())):
    lt = ["a","e","i","o","s"]
    en = [x.lower() for x in raw_input().strip()]
    r = 1
    for e in en:
        if lt.count(e) == 1:
            r *=3
        else:
            r *=2
    res.append(r)
for e in res:
    print e
