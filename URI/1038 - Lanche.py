p = [4.0,4.5,5.0,2.0,1.5]
e = [int(X) for X in raw_input().split()]

print "Total: R$ %.2f" % ((p[(e[0]-1)])*e[1])
