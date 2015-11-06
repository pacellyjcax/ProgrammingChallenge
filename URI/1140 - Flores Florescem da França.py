def ehTauto(s):
    s = s.lower()
    ls = s.split()
    tr = ls[0][0]
    for e in ls:
        if not e[0] == tr:
            return False
    return True


while 1:
    e= raw_input()
    if e == "*":
        break
    if ehTauto(e):
        print "Y"
    else:
        print "N"
