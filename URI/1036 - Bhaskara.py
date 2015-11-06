import math

e = [float(X) for X in raw_input().split()]

a = e[0]
b = e[1]
c = e[2]

d=pow(b,2)-4*a*c

if (2*a) == 0 or d<0:
    print "Impossivel calcular"
else:
    rd=math.sqrt(d)
    r1=(-b + (rd)) / (2 * a)
    r2=(-b - (rd)) / (2 * a)
    print "R1 = %.5f" % r1
    print "R2 = %.5f" % r2
    
