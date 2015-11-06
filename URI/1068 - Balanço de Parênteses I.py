while 1:
    try:
        en = raw_input()
        ok = []
        for e in en:
            if e == "(":
                ok.append(True)
            if e == ")":
                if len(ok)>0:
                    if ok[-1]:
                        ok.pop(-1)
                else:
                    ok.append(False)

        if len(ok) == 0:
            print "correct"
        else:
            print "incorrect"
    except:
        break
