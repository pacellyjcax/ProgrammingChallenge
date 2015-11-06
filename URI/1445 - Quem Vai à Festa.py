
while 1:
    n= int(raw_input())
    if n == 0:
        break
    e = [x for x in raw_input().split()]
    e = map(lambda x: x.replace("("," "),e)
    e = map(lambda x: x.replace(")"," "),e)
    e = map(lambda x: x.replace(","," "),e)
    d = {} 
    for x in e:
        co = x.split()
        if d.has_key(co[0]):
            d[co[0]].append(co[1])
        else:
            d[co[0]] = [co[1]]

#FALTA FAZER A CONTAGEM

    print len(lc)
