def calcula(l):
    return max(l)-min(l)

res = []
while 1:
    try:
        res.append(calcula([int(x) for x in raw_input().split()]))
    except:
        break

for e in res:
    print int(e)
