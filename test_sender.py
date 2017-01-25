import producer.filereader
import producer.dlstat
import formater.dlstat
import sender.stdout
import sender.stdouthint
import sender.graphite

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

for _ in range(10):
    sender_it.next()

producer_stream.close()
