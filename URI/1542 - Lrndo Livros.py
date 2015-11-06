import math

while 1:    
    n = raw_input()
    if n == "0":
        break   
    en = [float(x) for x in n.split()]
    
    qt = int((en[0]*en[1])/-(en[0]-en[2])*en[2])

    if qt == 1:
        print "1 pagina"
    else:
        print "%d paginas" %qt
