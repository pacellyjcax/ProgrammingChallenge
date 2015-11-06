e= int(raw_input())

f = [0,1]
for i in range(e-2):
    f.append(f[-1]+f[-2])

print str(f).replace("[","").replace("]","").replace(",","")


