def f(n):
    r = 0
    for i in range(1,n+1):
        r+=i**2
    return r
 
lf = []
 
while 1:
    N = int(raw_input())
    if N == 0:
        break
    lf.append(f(N))
 
for a in lf:
    print a
