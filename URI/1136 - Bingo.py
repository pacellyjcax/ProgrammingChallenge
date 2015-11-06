while 1:
    n, b = map(int, raw_input().split())
    if n == b == 0:
        break
    nums = map(int, raw_input().split())
    if 0 not in nums:
        print 'N'
        continue
    pos = set()
    for n1 in nums:
        for n2 in nums:
            pos.add(abs(n1 - n2))
    if len(pos) == n + 1:
        print 'Y'
    else:
        print 'N'
