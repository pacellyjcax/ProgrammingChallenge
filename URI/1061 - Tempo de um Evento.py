def s_end_day(h, m, s):
    return 86400 - (h * 3600) - (m * 60) - s

day_info = raw_input().split()
d1 = int(day_info[1])
h1, m1, s1 = map(int, raw_input().split(' : '))

day_info = raw_input().split()
d2 = int(day_info[1])
h2, m2, s2 = map(int, raw_input().split(' : '))

diff_sec = (d2 - d1) * 86400 + (s_end_day(h1, m1, s1) - s_end_day(h2, m2, s2))

print '%d dia(s)' % (diff_sec / 86400)
diff_sec %= 86400

print '%d hora(s)' % (diff_sec / 3600)
diff_sec %= 3600

print '%d minuto(s)' % (diff_sec / 60)
print '%d segundo(s)' % (diff_sec % 60)

#Versao com a falta da entrada formatada 
'''
import datetime

def horas_minutos_segundos(s):
    m = s/60
    s -= m*60
    h = m/60
    m -= h*60
    return [h,m,s]

di = int(raw_input().split()[1])
ti = raw_input().split()
hi = int(ti[0])
mi = int(ti[2])
si = int(ti[4])
df = int(raw_input().split()[1])
tf = raw_input().split()
hf = int(tf[0])
mf = int(tf[2])
sf = int(tf[4])

d1 = datetime.datetime(day=di, month=4, year=2015, hour=hi, minute=mi,second=sf)
d2 = datetime.datetime(day=df, month=4, year=2015, hour=hf, minute=mf,second=sf)


diff = d2-d1
print "%d dia(s)"%diff.days
t = horas_minutos_segundos(diff.seconds)
print "%d hora(s)"%t[0]
print "%d minuto(s)"%t[1]
print "%d segundo(s)"%t[2]
'''
