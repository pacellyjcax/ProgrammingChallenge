#versao com acesso a variavel
e = [int(X) for X in raw_input().split()]

a = int(e[0])
b = int(e[1])
c = int(e[2])
d = int(e[3])

if b>c and d>a and c+d>a+b and c>0 and d>0 and a%2==0:
    print "Valores aceitos"
else:
    print "Valores nao aceitos"

#versao com acesso direto (MAIS RAPIDA)
'''
e = [int(X) for X in raw_input().split()]

if e[1]>e[2] and e[3]>e[0] and e[2]+e[3]>e[0]+e[1] and e[2]>0 and e[3]>0 and e[0]%2==0:
    print "Valores aceitos"
else:
    print "Valores nao aceitos"
'''
