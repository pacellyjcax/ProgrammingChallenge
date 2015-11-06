line = raw_input().split()
a = float(line[0])
b = float(line[1])
c = float(line[2])
d = float(line[3])
media = (a * 2 + b * 3 + c * 4 + d * 1) / 10
print "Media: %.1f" % media
if (media > 7.0) :
    print "Aluno aprovado."
elif (media < 5.0) :
    print "Aluno reprovado."
else :
    print "Aluno em exame."
    nota = float(input())
    print "Nota do exame: " + str(nota)
    nota_final = (media + nota) / 2
    if nota_final < 5 :
        print "Aluno reprovado."
    else :
        print "Aluno aprovado."
    print "Media final: %.1f" % nota_final
