def Dva(n):
    return str((sum([int(n[i])*(i+1) for i in range(9)])%11))
def Dvb(n):
    return str((sum([int(n[i])*(9-i) for i in range(8,-1,-1)])%11))

while 1:
    try:
        e = raw_input()
        da = Dva(e)
        db = Dvb(e)
        if da == "10": da = "0"
        if db == "10": db = "0"
        print "{0:s}{1:s}{2:s}.{3:s}{4:s}{5:s}.{6:s}{7:s}{8:s}-{9:s}{10:s}".format(
            e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],da,db)
    except:
        break
