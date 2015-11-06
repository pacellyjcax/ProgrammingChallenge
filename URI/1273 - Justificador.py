res = []
while 1:
    d = int(raw_input())
    if d == 0:
        break
    res.append([raw_input() for i in range(d)])
    
for i in range(len(res)):
    tm = max([len(x) for x in res[i]])
    for k in res[i]:        
        esp = "".join([" " for j in range(tm-len(k))])
        print esp+k
    if i < len(res)-1:
        print

