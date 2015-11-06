def apaga(s,qt):
    ls = [int(x) for x in s]
    for i in range(qt):
        ls.remove(min(ls))
    return "".join([str(x)for x in ls])


while 1:
    e= raw_input()
    if e == "0 0":
        break
    print apaga(raw_input(),int(e.split()[1]))
