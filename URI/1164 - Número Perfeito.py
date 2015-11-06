def ehPerfeito(i):
    s = sum([x for x in range(1,i) if i%x == 0])
    if s == i:
        return True
    return False
    
e= int(raw_input())
for i in range(e):
    d = int(raw_input())
    if ehPerfeito(d):
        print "%d eh perfeito" %d
    else:
        print "%d nao eh perfeito" %d
