a = [float(x) for x in raw_input().split()]

if a[0]+a[1]>a[2] and a[0]+a[2]>a[1] and a[2]+a[1]>a[0]:
    print "Perimetro = %.1f" %(a[0]+a[1]+a[2])
else:
    print "Area = %.1f" %(((a[0]+a[1])*a[2])/2)
