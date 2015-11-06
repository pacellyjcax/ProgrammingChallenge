def rot13(s):
    if s.islower():
        if ord(s)+13>122:
            return chr(((ord(s)+13)-122)+96)
        return chr((ord(s)+13))
    if ord(s)+13>90:
        return chr(((ord(s)+13)-90)+64)
    return chr((ord(s)+13)) 

res = []
while 1:
    try:
        d = raw_input()
        r = ""
        for i in range(len(d)):
            if d[i].isalpha():

                r+=rot13(d[i])
            else:
                r += d[i]
        res.append(r)
    except:
        break
    
for e in res:
    print e

