def encaixa(l):
    dif = len(l[0])-len(l[1]) 
    if dif<0:
        return False
    if l[0][-len(l[1]):] == l[1]:
        return True
    return False

n = int(raw_input())
res = []

for i in range(n):
    e = raw_input().split()
    if encaixa(e):
        res.append("encaixa")
    else:
        res.append("nao encaixa")

for e in res:
    print e
