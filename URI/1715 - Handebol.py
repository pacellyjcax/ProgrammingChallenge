e = [int(x) for x in raw_input().split()]
jf = 0
for i in range(e[0]):
    j = [int(x) for x in raw_input().split() if int(x) == 0]
    if len(j)==0:
        jf+=1
print jf

