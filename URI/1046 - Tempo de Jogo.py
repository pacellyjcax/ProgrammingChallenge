e = [int(x) for x in raw_input().split()]
h1 = e[0]
h2 = e[1]

if h2 == 0:h2 = 24
if h2<h1:h2+=24

res = 0
if h1 == h2:
    res = 24
else:
    res = h2-h1



print "O JOGO DUROU {0:d} HORA(S)".format(res)
