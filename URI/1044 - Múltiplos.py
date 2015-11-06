a = [int(x) for x in raw_input().split()]

if max(a)%min(a) == 0:
    print "Sao Multiplos" 
else:
    print "Nao sao Multiplos" 
