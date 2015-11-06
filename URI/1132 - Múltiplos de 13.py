en = [int(raw_input()) for i in range(2)]
print sum([x for x in range(min(en),max(en)+1) if not x%13==0])
