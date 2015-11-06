#0.012
def sN(l):
    x = l[0]
    y = l[1]
    if ((y+1)-x)%2 == 0:
        return ((((y+1)-x)/2) * (x+y))
    return (((y-x)/2) * (x+(y-1)))+y

print sN([int(x)for x in raw_input().split()])

#0.016
'''
da = [int(x)for x in raw_input().split()]
if ((da[1]+1)-da[0])%2 == 0:
    print ((((da[1]+1)-da[0])/2) * (da[0]+da[1]))
else:
    print (((da[1]-da[0])/2) * (da[0]+(da[1]-1)))+da[1]
'''
#0.016
'''
def sN(x,y):
    if ((y+1)-x)%2 == 0:
        return ((((y+1)-x)/2) * (x+y))
    return (((y-x)/2) * (x+(y-1)))+y

da = [int(x) for x in raw_input().split()]
print sN(da[0],da[1])
'''
