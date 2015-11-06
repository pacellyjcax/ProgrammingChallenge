x = int(raw_input())
d = x
a = d/365
d -= a*365
m = d/30
d -= m*30
print '''{0:d} ano(s)
{1:d} mes(es)
{2:d} dia(s)'''.format(a,m,d)
