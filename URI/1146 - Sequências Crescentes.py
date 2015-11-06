it = []
while 1:
    x = int(raw_input())
    if x == 0:
        break
    s = "".join([str(y)+" " for y in range(1,x+1)])
    it.append("".join([s[i] for i in range(0,len(s)-1)]))

for e in it:
    print e
