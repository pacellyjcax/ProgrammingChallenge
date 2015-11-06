def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

n = int(raw_input())
for i in xrange(n):
    raw_input()
    en = [int(x) for x in raw_input().split()]
    en = qsort(en)
    s = ""
    for i in range(len(en)):
        s += str(en[i])
        if i < len(en)-1:
            s += " "
    print s

