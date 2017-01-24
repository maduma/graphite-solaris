import producer.filereader
import formater.dlstat

producer_stream = producer.filereader.get_stream('sample/dlstat.txt')

print("Period: " + str(producer_stream.period))
print("##########")

it = formater.dlstat.get_iterator(producer_stream)
for line in it:
    print line,

producer_stream.close()
