def printPar():
    for i in range(len(par)):
        print "par[{0:d}] = {1:d}".format(i,par[i])
def printImpar():
    for i in range(len(impar)):
        print "impar[{0:d}] = {1:d}".format(i,impar[i])
par = []
impar = []

for i in range(15):
    n= int(raw_input())
    if n%2 == 0:
        if len(par)<4:
            par.append(n)
        elif len(par)==4:
            par.append(n)
            printPar()
            par = []
    else:
        if len(impar)<4:
            impar.append(n)
        elif len(impar)==4:
            impar.append(n)
            printImpar()
            impar = []

if len(impar)>0:
    printImpar()
if len(par)>0:
    printPar()
