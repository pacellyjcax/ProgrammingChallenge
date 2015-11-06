def rafael(x,y):
    return pow((3.0*x),2) + pow(y,2)
def beto(x,y):
    return 2.0*pow(x,2) + pow((5*y),2)
def carlos(x,y):
    return -100.0*x + pow(y,3) 

pes = ["Rafael","Beto","Carlos"]
res = []

n = int(raw_input())
for i in range(n):
    en = raw_input().split()
    x = int(en[0])
    y = int(en[1])
    vs = [rafael(x,y),beto(x,y),carlos(x,y)]
    res.append(pes[vs.index(max(vs))])
            
for e in res:
    print e + " ganhou"
