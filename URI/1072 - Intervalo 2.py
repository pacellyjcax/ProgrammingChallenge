n = int(raw_input())
en = [int(raw_input()) for i in range(n)]
x = [e for e in en if e>=10 and e<=20]
print str(len(x))+" in"
print str(n-len(x))+" out"
