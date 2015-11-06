def calcula(v):
    vf = 1
    for i in range(1,v+1):
        vf *= i
    return vf
it = []
while 1:
    try:
        n = raw_input().split()
        it.append(calcula(int(n[0]))+calcula(int(n[1])))
    except:
        break
    

for e in it:
    print e
    
