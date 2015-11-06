en = [int(raw_input()) for i in range(5)]
par = [x for x in en if x%2==0]
imp = [x for x in en if x%2>0]
pos = [x for x in en if x>0]
neg = [x for x in en if x<0]

print '''{0:d} valor(es) par(es)
{1:d} valor(es) impar(es)
{2:d} valor(es) positivo(s)
{3:d} valor(es) negativo(s)'''.format(len(par),len(imp),len(pos),len(neg))
