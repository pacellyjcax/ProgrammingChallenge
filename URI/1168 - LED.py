def quantidade(s):
    ql = [2,5,5,4,5,6,3,7,6,6]
    return sum([ql[int(x)-1] for x in s.strip()])
    
e= int(raw_input())
res = []
for i in range(e):
    d = raw_input()
    res.append(quantidade(d))
    
for e in res:
    print "%d leds" %e
