def insereColuna():
    return [float(raw_input()) for i in range(12)]
mat = []
cl = int(raw_input())
op = raw_input()
for i in range(12):
    mat.append(insereColuna())

dcl = [x[cl] for x in mat]
if op == "S":
    print"%.1f" % (sum(dcl))
elif op == "M":
    
    print"%.1f" % (sum(dcl)/len(dcl))
