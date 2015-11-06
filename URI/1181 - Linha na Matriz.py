def insereLinha():
    return [float(raw_input()) for i in range(12)]
mat = []
li = int(raw_input())
op = raw_input()
for i in range(12):
    mat.append(insereLinha())

if op == "S":
    print"%.1f" % (sum(mat[li]))
elif op == "M":
    print"%.1f" % (sum(mat[li])/len(mat[li]))
