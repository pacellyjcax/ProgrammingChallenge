a = raw_input().split()
b = [float(x) for x in a]
print '''TRIANGULO: {0:.3f}
CIRCULO: {1:.3f}
TRAPEZIO: {2:.3f}
QUADRADO: {3:.3f}
RETANGULO: {4:.3f}'''.format(
    ((b[2]*b[0])/2),
(pow(b[2],2)*3.14159),
((b[2]*(b[0]+b[1]))/2.0),
(pow(b[1],2)),
(b[0]*b[1]))

