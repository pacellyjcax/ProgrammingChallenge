def insereLinha():
    return [float(raw_input()) for i in range(12)]
def somaElementos():
    c = 12
    s = 0.0
    for l in range(12):
	for x in range(c,12):
		s+=mat[l][x]
	c-=1 
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
