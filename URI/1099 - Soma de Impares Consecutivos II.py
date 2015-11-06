
def calcula():
    en = [int(X) for X in raw_input().split()]
    s = 0
    if min(en)%2==0:
        for i in range(min(en)+1,max(en),2):s+=i
    else:
        for i in range(min(en)+2,max(en),2):s+=i
    return s

res = [calcula() for i in range(int(raw_input()))]
for e in res:
    print e
