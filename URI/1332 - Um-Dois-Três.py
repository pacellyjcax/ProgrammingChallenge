def UmDoisTres(s):
    if len(s) == 5:
        return 3
    ls = [chr(i)+"ne" for i in range(ord("a"),ord("z")+1)]
    for i in range(ord("a"),ord("z")+1):ls.append("o"+chr(i)+"e")
    for i in range(ord("a"),ord("z")+1):ls.append("on"+chr(i))
    if ls.count(s):
        return 1
    return 2
    
res = []

n = int(raw_input())
for i in range(n):
    e = raw_input()
    res.append(UmDoisTres(e))

for e in res:
    print str(e)
