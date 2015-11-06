import locale

locale.setlocale(locale.LC_MONETARY, 'US')
res = []
while 1:
    try:
        en = [raw_input() for x in range(2)]
        if len(en[1]) == 1:
            en[1] = "0"+en[1]
        res.append(locale.currency(float(en[0]+"."+en[1]),grouping=True))
    except:
        break
    
for e in res:
    print e
