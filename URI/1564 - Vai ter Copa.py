res =[]
while 1:
    try:
        en = int(raw_input())
        if en > 0:
            res.append("vai ter duas!")
        else:
            res.append("vai ter copa!")
    except:
        break
for e in res:
    print e
