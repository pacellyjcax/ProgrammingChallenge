en = [int(x) for x in raw_input().split()]
s = 0
while 1:
    if en[1] <=0:
        en[1] = int(raw_input())
    else:
        for i in range(en[0],en[1]+1):
            s+=i
        print s
        break
