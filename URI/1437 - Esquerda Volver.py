def giro(ds):
    p = "N"
    for e in ds.strip():
        if e == "D":
            p = ps[p][0]
        else:
            p = ps[p][1]
    return p
        
res = []
ps = {"N":["L","O"],"S":["O","L"],"L":["S","N"],"O":["N","S"]}

while 1:
    n = int(raw_input())
    if n == 0:
        break    
    res.append(giro(raw_input()))

for e in res:
    print e
