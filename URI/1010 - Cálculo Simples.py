a = raw_input().split()
b = raw_input().split()
print "VALOR A PAGAR: R$ {0:.2f}".format((float(a[1]) * float(a[2]))
                                         +(float(b[1]) * float(b[2])))

