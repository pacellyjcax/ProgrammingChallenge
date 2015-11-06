e = float(raw_input())

if e<=2000:
    print "Isento"
elif e>2000 and e<=3000:
    e-=2000
    print "R$ %.2f"%(e*0.08)
elif e>3000 and e<=4500:
    e-=3000
    print "R$ %.2f"%((e*0.18)+(1000*0.08))
elif e>4500:
    e-=4500
    print "R$ %.2f"%((e*0.28)+(1500*0.18)+(1000*0.08))
