#0.0
def eB(l):
    if sum(l)>=(len(l)/2.):
        return "N"
    return "Y"

n = raw_input()
print eB([int(x)for x in raw_input().split()])
