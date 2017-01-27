import producer.zonestat
import formater.zonestat
import sender.graphite
import signal
import sys

producer_stream = producer.zonestat.get_stream(60)
formater_it = formater.zonestat.get_iterator(producer_stream)
sender_it = sender.graphite.get_iterator(formater_it)

def close_producer(signum=None, frame=None):
    if signum: print('Catching signal ' + str(signum))
    producer_stream.close()
    sys.exit()

# catch CTRL-C and unix kill
signal.signal(signal.SIGINT, close_producer)
signal.signal(signal.SIGTERM, close_producer)

for _ in sender_it: pass

close_producer()
