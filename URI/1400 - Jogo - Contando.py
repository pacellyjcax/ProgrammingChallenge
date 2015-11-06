def calcula(v):
    if v%7 ==0 or str(v).find("7")>=0:
        return True
    return False
        
it = []
while 1:
    en = raw_input()
    if en == "0 0 0":
        break
    daEn = en.split()
    vC = 1
    pJ = [i for i in range(1,int(daEn[0])+1)]
    for i in range(int(daEn[0])-1,1,-1):
        pJ.append(i)
    pO = int(daEn[1])
    qP = int(daEn[2])
    tPB = 0
    while vC<100:
        if pJ[0] == pO and calcula(vC):            
            tPB +=1
            if tPB == qP:
                break
        vC+=1
        pJ.append(pJ.pop(0))

    if vC==100:
        it.append(-1)
    else:
        it.append(vC)

for e in it:
    print e
