from math import sqrt

p1 = raw_input().split()
p2 = raw_input().split()
x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

print "{0:.4f}".format(sqrt( pow((x1-x2),2) + pow((y1-y2),2)))
