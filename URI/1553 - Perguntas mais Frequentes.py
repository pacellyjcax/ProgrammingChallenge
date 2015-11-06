while True:
    en = raw_input().split()
    if en[0] == "0" and en[1] == "0":
        break
    v = raw_input().split()
    d = {}
    for j in range(int(en[0])):
        d[str(j+1)] = 0

    for e in v:
        d[e] += 1

    vm = [x for x in d.values() if x >= int(en[1])]
    print len(vm)
