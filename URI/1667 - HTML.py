def formata(s):
    sf = ""
    s = s.replace("\n","")
    s = s.replace("<br>","\n")
    s = s.replace("<hr>","\n --------------------------------------------------------------------------------")   
    for i in range(len(s)):
        if [j for j in range(0,len(s)+1,80)].count(i) == 1 and not i==0:
            sf +="\n"
        sf += s[i]
    return sf


e= raw_input()
print formata(e)
