l = [float(x) for x in raw_input().split()]
m = (l[0] * 2 + l[1] * 3 + l[2] * 4 + l[3] * 1) / 10
print "Media: %.1f" % m
if m > 7.0 :
    print "Aluno aprovado."
elif m < 5.0 :
    print "Aluno reprovado."
else :
    print "Aluno em exame."
    n = float(raw_input())
    print "Nota do exame: " + str(n)
    nf = (m + n) / 2
    if nf < 5 :
        print "Aluno reprovado."
    else :
        print "Aluno aprovado."
    print "Media final: %.1f" % nf
