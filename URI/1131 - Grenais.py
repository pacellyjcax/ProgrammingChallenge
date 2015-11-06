def addGrenal(l):
    if l[0]>l[1]:
        g["Inter"]+=1
    elif l[0]<l[1]:
        g["Gremio"]+=1
    else:
        g["Empates"]+=1
        
g = {"Inter":0,"Gremio":0,"Empates":0}
addGrenal([int(x) for x in raw_input().split()])

while 1:
    print "Novo grenal (1-sim 2-nao)"
    n = int(raw_input())
    if n == 2:
        break
    elif n == 1:
        addGrenal([int(x) for x in raw_input().split()])


print'''{0:d} grenais
Inter:{1:d}
Gremio:{2:d}
Empates:{3:d}'''.format(g.get("Inter")+g.get("Gremio")+g.get("Empates"),g.get("Inter"),g.get("Gremio"),g.get("Empates"))
if g.get("Inter")>g.get("Gremio"):
    print "Inter venceu mais"
elif g.get("Inter")<g.get("Gremio"):
    print "Gremio venceu mais"
else:
    print "Nao houve vencedor"
