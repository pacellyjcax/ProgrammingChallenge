e = float(raw_input())
s = 0
r = 0
p = 0
if e >=0 and e<= 400:
    p = 15
    r = e*(0.15)
    s = e + r
elif e >400 and e<= 800:
    p = 12
    r = e*(0.12)
    s = e + r
elif e >800 and e<= 1200:
    p = 10
    r = e*(0.10)
    s = e + r
elif e >1200 and e<= 2000:
    p = 7
    r = e*(0.07)
    s = e + r
elif  e> 2000:
    p = 4
    r = e*(0.04)
    s = e + r

print "Novo salario: {0:.2f}".format(s)
print "Reajuste ganho: {0:.2f}".format(r)
print "Em percentual: {0:.0f} %".format(p)
