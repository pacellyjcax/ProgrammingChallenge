def inv(s):
    sf = ""
    for i in range(((len(s)/2)-1),-1,-1):
        sf += s[i]
    for i in range(len(s)-1,((len(s)/2)-1),-1):
        sf += s[i]
    return sf

res = []
for i in range(int(raw_input())):

    res.append(inv(raw_input()))
    
for e in res:
    print e
