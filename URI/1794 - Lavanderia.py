#0.0
def lav(n,la,lb,sa,sb):
    if la<=n<=lb and sa<=n<=sb:
        return "possivel"
    return "impossivel"

n = int(raw_input())
l = [int(x)for x in raw_input().split()]
s = [int(x)for x in raw_input().split()]

print lav(n,l[0],l[1],s[0],s[1])
