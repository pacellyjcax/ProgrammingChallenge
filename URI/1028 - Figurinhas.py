def calcula(v1, v2):
    if v2 == 0:
        return v1
    else:
        return calcula(v2, v1 % v2)

it = []
n = int(raw_input())
for i in range(n):
    b = raw_input().split()
    it.append([int(x) for x in b])

for e in it:
    print calcula(e[0],e[1])

    
