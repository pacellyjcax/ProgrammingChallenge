d = {"vertebrado":
         {"ave":
                {"carnivoro":"aguia","onivoro":"pomba"},
          "mamifero":
                {"onivoro":"homem","herbivoro":"vaca"}},
    "invertebrado":
          {"inseto":
                {"hematofago":"pulga","herbivoro":"lagarta"},
           "anelideo":
                {"hematofago":"sanguessuga","onivoro":"minhoca"}}}
e0 = raw_input()
e1 = raw_input()
e2 = raw_input()
print d[e0][e1][e2]
