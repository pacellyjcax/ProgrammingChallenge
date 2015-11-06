res = []
n = int(raw_input())
for i in range(n):
    tmat =int(raw_input())
    mat = [[int(x) for x in raw_input().split()] for k in range(tmat)]
    
    for j in range(len(mat)):
        for k in range(len(mat)):
            mat[j][k] *= mat[j][k]
    
    for k in range(len(mat)):
        tm = max([len(str(mat[x][k])) for x in range(len(mat))])
        for j in range(len(mat)):
            ta = len(str(mat[j][k]))
            if ta<tm:
                mat[j][k] = "".join([" " for x in range(tm-ta)])+str(mat[j][k])
            else:
                mat[j][k] = str(mat[j][k])
   
    res.append(mat)


for i in range(len(res)):
    print "Quadrado da matriz #%d:" %(i+4)
    for e in res[i]:
        strF = str(e).replace(",","")
        strF = strF.replace("'","")
        strF = strF.replace("[","")
        strF = strF.replace("]","")
        print strF
    if i< len(res)-1:
        print
