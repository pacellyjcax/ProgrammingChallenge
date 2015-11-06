d = {"A":0,"G":0,"D":0}
while 1:
    en = int(raw_input())
    if en == 4:
        break
    elif en == 1:
        d["A"]+=1
    elif en == 2:
        d["G"]+=1
    elif en == 3:
        d["D"]+=1
    
print '''MUITO OBRIGADO
Alcool: {0:d}
Gasolina: {1:d}
Diesel: {2:d}'''.format(d["A"],d["G"],d["D"])
