import producer.filereader
import producer.dlstat
import formater.dlstat
import producer.iostat
import formater.iostat
import os

PKGDIR = os.path.dirname(os.path.realpath(__file__))
producer_stream = producer.filereader.get_stream(PKGDIR + '/sample/dlstat.txt')

print('### filereader')
print('Period: ' + str(producer_stream.period))
print('###')

for line in formater.dlstat.get_iterator(producer_stream):
    print line

producer_stream.close()

### --- ###

producer_stream = producer.dlstat.get_stream(1)

print('### dlstat')
print('Period: ' + str(producer_stream.period))
print('###')

it = formater.dlstat.get_iterator(producer_stream)

for _ in range(30):
    print it.next()

producer_stream.close()

### --- ###

producer_stream = producer.iostat.get_stream(1)

print('### iostat')
print('Period: ' + str(producer_stream.period))
print('###')

it = formater.iostat.get_iterator(producer_stream)

for _ in range(30):
    print it.next()

producer_stream.close()

