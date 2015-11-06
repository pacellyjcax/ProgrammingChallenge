def Dva(n):
    return str((sum([int(n[i])*(i+1) for i in range(9)])%11))
def Dvb(n):
    return str((sum([int(n[i])*(9-i) for i in range(8,-1,-1)])%11))

res = []
while 1:
    try:
        en = raw_input().split("-")
        cpfIni = en[0].replace(".","")
        da = Dva(cpfIni)
        db = Dvb(cpfIni)
        if da == "10": da = "0"
        if db == "10": db = "0"
        if da == en[1][0] and  db == en[1][1]:
            res.append("CPF valido")
        else:
            res.append("CPF invalido")
    except:
        break


for e in res:
    print e
