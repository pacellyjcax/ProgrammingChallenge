def insereLinha():
    return [float(raw_input()) for i in range(12)]
def somaElementos():
    i = 0
    f = 1
    s = 0.0
    for l in range(1,6):
	for x in range(i,f):
		s+=mat[l][x]
	f += 1
    f = 5
    for l in range(6,11):
	for x in range(i,f):
		s+=mat[l][x]
	f -= 1
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
