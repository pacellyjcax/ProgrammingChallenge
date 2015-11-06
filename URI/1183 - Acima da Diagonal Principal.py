#fuleragem de runtime
'''def insereLinha():
    return [float(raw_input()) for i in range(12)]

mat = []

op = raw_input()
for i in range(12):
    mat.append(insereLinha())

elDP = []
c = 1
for l in range(len(mat)):
    eldp.append([mat[l][x] for x in range(c,12)])
    c+=1

somaElDP = (sum([sum(e) for e in elDP]))
if op == "S":
    print"%.1f" % somaElDP
elif op == "M":
    
    print"%.1f" % (somaElDP/66.0)'''

#Algoritmo SEU LUNGA
def insereLinha():
    return [float(raw_input()) for i in range(12)]
def somaElementos():
    s = 0.0
    s += mat[0][1]
    s += mat[0][2]
    s += mat[0][3]
    s += mat[0][4]
    s += mat[0][5]
    s += mat[0][6]
    s += mat[0][7]
    s += mat[0][8]
    s += mat[0][9]
    s += mat[0][10]
    s += mat[0][11]
    s += mat[1][2]
    s += mat[1][3]
    s += mat[1][4]
    s += mat[1][5]
    s += mat[1][6]
    s += mat[1][7]
    s += mat[1][8]
    s += mat[1][9]
    s += mat[1][10]
    s += mat[1][11]
    s += mat[2][3]
    s += mat[2][4]
    s += mat[2][5]
    s += mat[2][6]
    s += mat[2][7]
    s += mat[2][8]
    s += mat[2][9]
    s += mat[2][10]
    s += mat[2][11]
    s += mat[3][4]
    s += mat[3][5]
    s += mat[3][6]
    s += mat[3][7]
    s += mat[3][8]
    s += mat[3][9]
    s += mat[3][10]
    s += mat[3][11]
    s += mat[4][5]
    s += mat[4][6]
    s += mat[4][7]
    s += mat[4][8]
    s += mat[4][9]
    s += mat[4][10]
    s += mat[4][11]
    s += mat[5][6]
    s += mat[5][7]
    s += mat[5][8]
    s += mat[5][9]
    s += mat[5][10]
    s += mat[5][11]
    s += mat[6][7]
    s += mat[6][8]
    s += mat[6][9]
    s += mat[6][10]
    s += mat[6][11]
    s += mat[7][8]
    s += mat[7][9]
    s += mat[7][10]
    s += mat[7][11]
    s += mat[8][9]
    s += mat[8][10]
    s += mat[8][11]
    s += mat[9][10]
    s += mat[9][11]
    s += mat[10][11]
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
