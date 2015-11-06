import math

def ff(l):
    if math.sqrt( pow((l[1]-l[4]),2) + pow((l[2]-l[5]),2) ) + l[3] <= l[0]:
        return "RICO"
    return "MORTO"

while 1:
    try:
        print ff([float(x) for x in raw_input().split()])
    except:
        break
