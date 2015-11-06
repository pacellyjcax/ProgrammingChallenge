def avanca(s,qt):
    if ord(s)+qt > 122:
        return chr(((ord(s)+qt)-122)+96)
    return chr(ord(s)+qt)

res = []
n = int(raw_input())
for i in range(n):
    t = 0
    en = raw_input().split()
    for i in range(len(en[0])):
        if en[0][i] == en[1][i]:
            continue
        else:
            for j in range(1,26):
                if avanca(en[0][i],j) == en[1][i]:
                    t += j
                    break
    res.append(t)

for e in res:
    print e
                    
