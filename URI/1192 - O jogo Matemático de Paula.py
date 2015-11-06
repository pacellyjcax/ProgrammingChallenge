def calcula(l):
    n1 = int(l[0])
    n2 = int(l[2])
    op = l[1]
    if n1 == n2:
        return n1*n2
    elif op.islower():
        return n1+n2
    return n2-n1

res = []

n = int(raw_input())
for i in range(n):
    res.append(calcula(raw_input().strip()))

for e in res:
    print e
