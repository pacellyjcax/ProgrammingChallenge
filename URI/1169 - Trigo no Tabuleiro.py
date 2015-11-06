def calcula(x):
    r = 1
    t = 1
    for i in range(1,x+1):
        t += r*2
        r *= 2
    return (r/12)/1000
vf = []
x = int(raw_input())
for i in range(x):
    vf.append(calcula(int(raw_input())))

for e in vf:
    print "{0:d} kg".format(e)
