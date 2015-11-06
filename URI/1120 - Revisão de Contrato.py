def calcula(lX):
    lf = [v for v in lX[1].strip() if v!= lX[0]]
    if len(lf) == 0:
        return 0
    return int("".join(lf))
        
            
it = []
while 1:
    d = raw_input()
    if d == "0 0":
        break
    it.append(calcula(d.split()))

for e in it:
    print e
