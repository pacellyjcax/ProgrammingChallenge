def crypto(strX):
    a = list(strX)
    for i in range(len(a)):
        if a[i].isalpha():
            a[i] = chr((ord(a[i])+3))
    a.reverse()
    for i in range((len(a)/2),len(a)):
        a[i] = chr((ord(a[i])-1))

    return "".join(a)
        
            
en = []
n = int(raw_input())
for i in range(n):
    en.append(crypto(raw_input()))
for e in en:
    print e
