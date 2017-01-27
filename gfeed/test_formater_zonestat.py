import producer.filereader
import formater.zonestat
import os

PKGDIR = os.path.dirname(os.path.realpath(__file__))
producer_stream = producer.filereader.get_stream(
    PKGDIR + '/sample/zonestat.txt')

print('### filereader')
print('Period: ' + str(producer_stream.period))
print('###')

for line in formater.zonestat.get_iterator(producer_stream):
    print line

producer_stream.close()
