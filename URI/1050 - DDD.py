d = {
     61:"Brasilia",
     71:"Salvador",
     11:"Sao Paulo",
     21:"Rio de Janeiro",
     32:"Juiz de Fora",
     19:"Campinas",
     27:"Vitoria",
     31:"Belo Horizonte"
    }
e = int(raw_input())

if d.has_key(e):
    print d[e]
else:
    print "DDD nao cadastrado"
