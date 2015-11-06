import math
def calcula(l):
    return int(math.sqrt((l[0]*l[1]*100)/l[2]))


res = []

while 1:
    en = raw_input()
    if en == "0":
        break
    da = [int(x) for x in en.split()]
    res.append(calcula(da))
            
for e in res:
    print e
