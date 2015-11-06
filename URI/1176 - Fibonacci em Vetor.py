def fib(i):
    while i >= len(f)-1:
        f.append(f[-1]+f[-2])
    return f[i]

f = [0,1]
res = []
n= int(raw_input())
for i in range(n):
    e= int(raw_input())
    res.append("Fib({0:d}) = {1:d}".format(e,fib(e)))

for e in res:
    print e
