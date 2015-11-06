x= int(raw_input())

while 1:
    z= int(raw_input())
    if z>x:
        break
s = 0
c = 1
for i in range(x,z+1):
    s+=i
    if s>z:
        print c
        break
    c+=1
