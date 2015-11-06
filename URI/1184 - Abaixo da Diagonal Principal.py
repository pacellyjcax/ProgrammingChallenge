'''def insereLinha():
    return [float(raw_input()) for i in range(12)]

mat = []

op = raw_input()
for i in range(12):
    mat.append(insereLinha())

elDP = []
c = 0
for l in range(len(mat)):
    eldp.append(sum([mat[l][x] for x in range(0,c)]))
    c+=1

somaElDP = sum(elDP)
if op == "S":
    print"%.1f" % somaElDP
elif op == "M":
    
    print"%.1f" % (somaElDP/66.0)'''

def insereLinha():
    return [float(raw_input()) for i in range(12)]
def somaElementos():
    c = 0
    s = 0.0
    for l in range(12):
	for x in range(0,c):
		s+=mat[l][x]
	c+=1 
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
