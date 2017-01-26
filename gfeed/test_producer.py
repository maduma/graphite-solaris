import itertools
import producer.filereader
import producer.cmdreader
import producer.iostat
import producer.zonestat
import os

PKGDIR = os.path.dirname(os.path.realpath(__file__))

st1 = producer.filereader.get_stream(PKGDIR + '/sample/dlstat.txt')
st2 = producer.cmdreader.get_stream(['/usr/bin/vmstat', '1'], 1)
st3 = producer.iostat.get_stream(1)
st4 = producer.zonestat.get_stream(1)

print(st1.period)
print(st2.period)
print(st3.period)
print(st4.period)

st = itertools.izip(st1.it, st2.it, st3.it, st4.it)

for _ in range(10):
    lines = st.next()
    print ''.join(lines),

st1.close()
st2.close()
st3.close()
st4.close()
