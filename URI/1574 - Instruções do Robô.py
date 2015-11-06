'''
def move(ac):
    global p
    if ac == "LEFT":        
        p -= 1
        acs.append(ac)
    elif ac == "RIGHT":
        p += 1
        acs.append(ac)

p = 0
acs = []
res = []

n = int(raw_input())
for i in range(n):
    n = int(raw_input())
    for i in range(n):
        acao = raw_input()
        if acao[0] == "S":
            move(acs[int(acao.split()[2])-1])
        else:
            move(acao)
        print acs
    res.append(p)
    p = 0
    acs = []
    
for e in res:
    print e
'''
def move(ac):
    global p
    if ac == "LEFT":        
        p -= 1
        acs.append(ac)
    elif ac == "RIGHT":
        p += 1
        acs.append(ac)
    else:
        acA = acs[int(ac[-1])-1]
        move(acA)
 
p = 0
acs = []
res = []
 
n = int(raw_input())
for i in range(n):
    n = int(raw_input())
    for i in range(n):
        move(raw_input())
    res.append(p)
    p = 0
    acs = []
     
for e in res:
    print e 
