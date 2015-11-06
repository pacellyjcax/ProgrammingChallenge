en = [int(raw_input()) for i in range(2)]
s = 0
if min(en)%2==0:
    for i in range(min(en)+1,max(en)+1,2):s+=i
else:
    for i in range(min(en)+2,max(en),2):s+=i
print s
