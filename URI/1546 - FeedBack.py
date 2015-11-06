res = []

pes = ["Rolien","Naej","Elehcim","Odranoel"]

n = int(raw_input())
for i in range(n):
    k = int(raw_input())
    for i in range(k):
        res.append(pes[int(raw_input())-1])
            
for e in res:
    print e
