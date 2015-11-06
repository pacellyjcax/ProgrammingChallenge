# -*- coding: utf-8 -*-
 
e = 0
res = []
while 1:
    e = int(raw_input())
     
    if e == 2002:
        res.append("Acesso Permitido")
        break 
    else:
        res.append("Senha Invalida")
 
for e in res:
    print e
