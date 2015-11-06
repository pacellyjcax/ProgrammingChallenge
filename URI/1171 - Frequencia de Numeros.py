e= int(raw_input())
res = {}
for i in range(e):
    d = int(raw_input())
    if res.has_key(d):
        res[d]+=1
    else:
        res[d]=1
    
for i in range(len(res.keys())):
    print str(min(res.keys()))+" aparece "+str(res.pop(min(res.keys())))+" vez(es)"
  
