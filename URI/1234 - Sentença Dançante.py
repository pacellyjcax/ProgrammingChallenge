def danca(s,op):
    if op%2 ==0:
        return s.upper()
    return s.lower()
        

res = []
while 1:
    try:
        d = raw_input()
        op = 1
        r = ""
        for i in range(len(d)):
            if d[i].isalpha():
                op+=1
                r+=danca(d[i],op)
            else:
                r += d[i]
        res.append(r)
    except:
        break
    
for e in res:
    print e
