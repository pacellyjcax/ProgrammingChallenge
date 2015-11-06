x = int(raw_input())
s = x
m = s/60
s -= m*60
h = m/60
m -= h*60
print "{0:d}:{1:d}:{2:d}".format(h,m,s)
