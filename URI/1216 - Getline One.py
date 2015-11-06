res = []
while 1:
    try:
        raw_input()
        res.append(float(raw_input()))
    except:
        break


print "%.1f" %(sum(res)/len(res))
