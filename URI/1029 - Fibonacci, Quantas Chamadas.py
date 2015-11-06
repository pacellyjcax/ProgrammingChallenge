def fib(v):
    global c
    c+=1
    if v == 0 or v == 1:
        return v
    else:
        return fib(v-1)+fib(v-2)

n = int(raw_input())
for i in xrange(n):
    en = int(raw_input())
    c = -1
    r = fib(en)
    print "fib({0:d}) = {1:d} calls = {2:d}".format(en,c,r)
