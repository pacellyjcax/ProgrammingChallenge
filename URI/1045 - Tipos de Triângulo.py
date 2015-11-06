a = [float(x) for x in raw_input().split()]
a.sort()
a.reverse()


if a[0]>=a[1]+a[2]:
    print "NAO FORMA TRIANGULO"
else:
    if pow(a[0],2)==pow(a[1],2)+pow(a[2],2):
        print "TRIANGULO RETANGULO"
    if pow(a[0],2)>pow(a[1],2)+pow(a[2],2):
        print "TRIANGULO OBTUSANGULO"
    if pow(a[0],2)<pow(a[1],2)+pow(a[2],2):
        print "TRIANGULO ACUTANGULO"
    if a[0]==a[1]==a[2]:
        print "TRIANGULO EQUILATERO"
    elif a[0]==a[1] or a[0]==a[2] or a[2]==a[1]:
        print "TRIANGULO ISOSCELES"
