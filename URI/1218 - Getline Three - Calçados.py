def calcula(l,c):
    m = 0
    f = 0
    for i in range(0,len(l),2):
        if l[i] == c:
            if l[i+1] == "M":
                m+=1
            elif l[i+1] == "F":
                f+=1
    return (f,m)

res = [] 
while 1:
    try:
        n = raw_input()
        res.append(calcula(raw_input().split(),n))
    except:
        break

for i in range(len(res)):
    print '''Caso {0:d}:
Pares Iguais: {1:d}
F: {2:d}
M: {3:d}'''.format(i+1,res[i][0]+res[i][1],res[i][0],res[i][1])
    if i < len(res)-1:
        print 

    

