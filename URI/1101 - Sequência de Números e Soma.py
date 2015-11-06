
def calcula(en):
    s = 0
    st = ""
    for i in range(min(en),max(en)+1):
        s+=i
        st+=str(i)+" "
    st+="Sum=%d"%s
    return st
res =[]
while 1:
    en = [int(X) for X in raw_input().split()]
    if en[0]<=0 or en[1]<=0:
        break
    res.append(calcula(en))
    
for e in res:
    print e
