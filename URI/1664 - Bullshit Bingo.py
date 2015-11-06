def bullshitBingo(s):
    sf = "".join([x for x in s if x.isalpha()==True or x==" "])
    da = sf.split("BULLSHIT")
    if not sf[-8:] == "BULLSHIT":
        da.pop(-1)
    dat = [x.split() for x in da]
    daf = []
    for e in dat:
        daf.append([x for x in e if x.isalpha()==True])
    tj = len(daf)
    tp = sum([len(x) for x in dat])
    return (tp,tj)

def mdc(d, div):
    if div == 0:
        return d
    else:
        return mdc(div, d % div)

en= raw_input()

tp,tj = bullshitBingo(en)
m = mdc(tp,tj)
if m > 0:
    print "%d / %d" %((tp/m),(tj/m))
else:
    print "%d / %d" %(tp,tj)
        
