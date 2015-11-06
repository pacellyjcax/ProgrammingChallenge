def subst(s,t,tf):
    st = ""
    pi = 0
    sit = False
    i = 0
    while i < len(s):
        if sit:
            st+=s[i]
        if s[i] == "<":
            sit = True
            pi = i
        elif s[i] == ">":
            sit = False
            t = t.lower()
            st = st.lower()
            st = st.replace(t,tf)
            s = s[:pi+1]+st+s[i+1:]
            st = ""
        i+=1
    return s


print subst("<><BODY garbage>body</BODY>","BODY","10")
print subst("<dont replacethis>abcabc<abcabcde>","aBc","923")
print subst("<ta>bLe<TaBlewidth=100></table></ta>","table","1")
print subst("nothing inside","replace","323")
print subst("92<HI=/><z==//HIb><cHIhi> ","HI","667")
print subst("<a B c a>","a","23")
print subst("<b b abc ab c> Mangojata","b","2")

            
