def insereLinha():
    return [float(raw_input()) for i in range(12)]
def somaElementos():
    i = 5
    f = 7
    s = 0.0
    for l in range(7,12):
	for x in range(i,f):
		s+=mat[l][x]
	i -= 1
	f += 1
    return s
    

mat = []

op = raw_input()
for i in range(12):
    mat.append(insereLinha())

somaEl = somaElementos()
if op == "S":
    print"%.1f" % somaEl
elif op == "M":
    
    print"%.1f" % (somaEl/66.0)
