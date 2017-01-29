import chunker.separatorline_map
import socket
import re
import subprocess
import time
from .. import config

prefix = '{0}.{1}.{2}'.format(
    config.LABEL, socket.gethostname(), config.IOSTAT)

device2poolmap = {}

iostat_pattern =  re.compile(r'(\d+\.\d+,){8}(\d+,){2}\S+')

def updatedevice2zpoolmap():
    if ('lastupdate' in device2poolmap
        and time.time() - device2poolmap['lastupdate'] < 3600): return
    cmd = 'timeout 30 /usr/sbin/zpool status -Tu'
    output = subprocess.Popen(
        cmd ,shell=True, stdout=subprocess.PIPE).communicate()[0]
    line_it = iter(output.splitlines(True))
    pattern = re.compile('^\d{10}$')
    chunks = chunker.separatorline.get_iterator(
        line_it, pattern, discard_first=False)
    device_pattern = re.compile('^\s+c\d+t\w+d\d+\s.*')
    for chunk in chunks:
        zpool = chunk[1][8:].rstrip()
        for line in chunk:
            if device_pattern.match(line):
                device = line.split()[0]
        device2poolmap[device] = zpool
        device2poolmap['lastupdate'] = time.time()

def transform(chunk):
    updatedevice2zpoolmap()
    epoch = chunk.pop(0).rstrip()

    for line in chunk:
        if not iostat_pattern.match(line): continue

        fields = line.rstrip().split(',')
        (rs, ws, krs, kws) = fields[:4]
        (asvct, _, busy, device) = fields[-4:]
        ops = str(float(rs) + float(ws))
        kbs = str(float(krs) + float(kws))
        
        if ':' in device:
            type_name = ['nfs', device.split(':')[0].replace('.', '_')]
            device = device.split(':')[1].lstrip('/').replace('/', '_')
        else:
            name = device2poolmap.get(device, None)
            if name:
                type_name = ['zpool' , name] 
            else:
                type_name = ['none']
        type_name = '.'.join(type_name)

        msg = '{0}.{1}.{2}.{{0}} {{1}} {3}'.format(
            prefix, type_name, device, epoch)

        yield msg.format('rs', rs)
        yield msg.format('ws', ws)
        yield msg.format('krs', krs)
        yield msg.format('kws', kws)
        yield msg.format('asvct', asvct)
        yield msg.format('busy', busy)
        yield msg.format('ops', ops)
        yield msg.format('kbs', kbs)

    yield config.HINT # usefull hint for consumer

def get_iterator(stream):
    pattern = re.compile('^\d{10}$')
    return chunker.separatorline_map.get_iterator(
        stream.lines, pattern, transform)
