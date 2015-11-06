def isTuring(s):
    s1 =s.split("=")[0]
    s2 =s.split("=")[1]
    st1 = s1[::-1]
    sf2 = int(s2[::-1])
    sf1 = sum([int(x) for x in st1.split("+")])
    if sf1 == sf2:
        return True
    return False

res = []
while 1:
    n = raw_input()
    if n == "0+0=0":
        res.append(isTuring(n))
        break
    res.append(isTuring(n))

for e in res:
    print e
                    
