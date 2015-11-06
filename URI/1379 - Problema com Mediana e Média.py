while 1:
    en = [int(x) for x in raw_input().split()]
    if en[0] == 0 and en[1] == 0:
        break
    if en[0] < en[1]:
        print (en[0]-(en[1]-en[0]))
    else:
        print (en[1]-(en[0]-en[1]))
