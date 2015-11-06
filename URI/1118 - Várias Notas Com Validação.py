def valida(n):
    if n >= 0 and n <= 10:
        return True
    return False

while 1:
    ns = [0,0]
    for i in range(2):
        while 1:
            ns[i] = float(raw_input())
            if valida(ns[i]):
                break
            print "nota invalida"
    print "media = %.2f" %((ns[0]+ns[1])/2.0)
    mn = 0
    while 1:
        print "novo calculo (1-sim 2-nao)"
        mn = int(raw_input())
        if mn == 1 or mn==2:
            break
    if mn == 2:
        break
        
