import producer.filereader
import producer.cmdreader
import producer.iostat

st1 = producer.filereader.stream('sample/dlstat.txt')
st2 = producer.cmdreader.stream(['/usr/bin/vmstat', '1'], 1)
st3 = producer.iostat.stream(1)
print(st1.period)
print(st2.period)
print(st3.period)

for _ in range(10):
    line = st1.it.next()
    print line,
    line = st2.it.next()
    print line,
    line = st3.it.next()
    print line,

st1.close()
st2.close()
st3.close()
