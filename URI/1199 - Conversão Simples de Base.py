it = []
while 1:
    v = raw_input()
    if v[0]== "-":
        break
    if v.isdigit():
        it.append(str(hex(int(v))))            
    else:
        it.append(str(int(v,16)))
for e in it:
    print e
