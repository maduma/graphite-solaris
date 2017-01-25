import producer.filereader
import producer.dlstat
import formater.dlstat
import sender.stdout
import sender.stdouthint
import sender.graphite
import signal
import sys
import time

producer_stream = producer.filereader.get_stream('sample/dlstat.txt')
formater_it = formater.dlstat.get_iterator(producer_stream)
sender_it = sender.stdout.get_iterator(formater_it)

for _ in sender_it: pass

producer_stream.close()

### --- ###

producer_stream = producer.filereader.get_stream('sample/dlstat.txt')
formater_it = formater.dlstat.get_iterator(producer_stream)
sender_it = sender.stdouthint.get_iterator(formater_it)

for _ in sender_it: pass

producer_stream.close()


### --- ###

producer_stream = producer.dlstat.get_stream(60)
formater_it = formater.dlstat.get_iterator(producer_stream)
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
