n= int(raw_input())

if n>1:
    d = [int(x) for x in raw_input().split()]
    mv = d[0]
    ind = 0
    for i in range(1,n):
        if d[i]<= mv:
            mv = d[i]
            ind = i
else:
    mv = int(raw_input())
    ind = 0

print "Menor valor: "+str(mv)
print "Posicao: "+str(ind)

# Solucao 1

'''
n= int(raw_input())
d = [int(x) for x in raw_input().split()]
print''Menor valor: {0:d}
Posicao: {1:d}''.format(min(d),d.index(min(d)))
'''
