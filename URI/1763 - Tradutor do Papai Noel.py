p = {}
p["brasil"] = "Feliz Natal!"
p["alemanha"] = "Frohliche Weihnachten!"
p["austria"] = "Frohe Weihnacht!"
p["coreia"] = "Chuk Sung Tan!"
p["espanha"] = "Feliz Navidad!"
p["grecia"] = "Kala Christougena!"
p["estados-unidos"] = "Merry Christmas!"
p["inglaterra"] = "Merry Christmas!"
p["australia"] = "Merry Christmas!"
p["portugal"] = "Feliz Natal!"
p["suecia"] = "God Jul!"
p["turquia"] = "Mutlu Noeller"
p["argentina"] = "Feliz Navidad!"
p["chile"] = "Feliz Navidad!"
p["mexico"] = "Feliz Navidad!"
p["antardida"] = "Merry Christmas!"
p["canada"] = "Merry Christmas!"
p["irlanda"] = "Nollaig Shona Dhuit!"
p["belgica"] = "Zalig Kerstfeest!"
p["italia"] = "Buon Natale!"
p["libia"] = "Buon Natale!"
p["siria"] = "Milad Mubarak!"
p["marrocos"] = "Milad Mubarak!"
p["japao"] = "Merii Kurisumasu!"

#imprimindo direto
while 1:
    try:
        e = raw_input()
        if p.has_key(e):
            print p[e]
        else:
            print "--- NOT FOUND ---"
    except:
        break

#Salvando respostas
'''
res = []
while 1:
    try:
        e = raw_input().lower()
        if p.has_key(e):
            res.append(p[e])
        else:
            res.append("--- NOT FOUND ---")
    except:
        break

for e in res:
    print e
'''
