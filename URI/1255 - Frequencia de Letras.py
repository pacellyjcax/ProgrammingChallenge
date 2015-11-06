res = []

n = int(raw_input())
for i in range(n):
    en = raw_input()
    en = en.lower()
    d = {}
    for e in en:
        if e.isalpha():
            if d.has_key(e):
                d[e] += 1
            else:
                d[e] = 1
    vm = max(d.values())
    lt = []
    for (k,v) in d.items():
        if v == vm:
            lt.append(k)
    lt.sort()
    res.append("".join(lt))

for e in res:
    print e
