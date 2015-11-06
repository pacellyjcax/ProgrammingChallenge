import datetime
def converte(s):
    m = s/60
    s -= m*60
    h = m/60
    m -= h*60
    return (h,m)

e = [int(x) for x in raw_input().split()]
h1 = e[0]
m1 = e[1]
h2 = e[2]
m2 = e[3]
d = 25
fi = ()

if h1 == h2 and m1 == m2:
    fi = (24,0)
elif h2<h1 or (h2 == h1 and m2<m1):
    d1 = datetime.datetime(day=d, month=3, year=2014,hour=h1,minute=m1)
    d2 = datetime.datetime(day=(d+1), month=3, year=2014,hour=h2,minute=m2)
    df = d2-d1
    fi = converte(df.seconds)
else:
    d1 = datetime.datetime(day=d, month=3, year=2014,hour=h1,minute=m1)
    d2 = datetime.datetime(day=d, month=3, year=2014,hour=h2,minute=m2)
    df = d2-d1
    fi = converte(df.seconds)

print "O JOGO DUROU {0:d} HORA(S) E {1:d} MINUTO(S)".format(fi[0],fi[1])
