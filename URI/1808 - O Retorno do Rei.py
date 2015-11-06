#0.0
def oRdR(s):
    q10 = s.count("0")
    s = s.replace("0","9")
    t = [int(x) for x in s]
    return float(sum(t))/(len(t)-q10)

print "%.2f"%oRdR(raw_input())
