while 1:
    a, b = map(int, raw_input().split())
    if a == b == 0:
        break
    ca = map(int, raw_input().split())
    cb = map(int, raw_input().split())
    op1 = len(set(ca) - set(cb))
    op2 = len(set(cb) - set(ca))

    print min(op1, op2)
