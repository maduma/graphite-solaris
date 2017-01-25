# Solaris system stat to graphite

This program basicaly does this 3 task

- Read data from a solaris stat command (e.g zonestat, iostat, ...)
- Transform the value to graphite format (e.g lable value time)
- Send stat to graphite via the nerwork

PRODUCE STAT -> TRANSFORM DATA -> SEND TO GRAPHITE

## Produce the stat
We rely on an external os command to produce the stat
- iostat (disk)
- zonestat (memory, cpu, network per zone) 
- dlstat (network per interface)
- vmstat (cpu)
- ...

The main logic is to run the program with parameters and read the output
produced. Basicaly they are two input in this stage.

### output
- character line stream
- period of stat (e.g 60 sec)

## Tranform the data
We get the stream procuced in the first step and transform the data in graphite format.
This module is also repossible for adding 'tags' to the stat (e.g hostname, zpool) and
may also create new stat based on the input (e.g total bytes = rbytes + wbytes).
We can also normalize stat here (e.g op/s, byte/s)

### input (output of the previous task)
- stream (line)
- period in second

# output
- stream (line in graphite format)

# implementaion detail
Streams will be implemented using iterator

# test
```
python -m gfeed.test_producer
python -m gfeed.test_formater
python -m gfeed.test_sender
```
