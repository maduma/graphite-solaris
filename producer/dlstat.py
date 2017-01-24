# dlstat reader iterator
import cmdreader

def get_stream(period):

    cmd = ['/usr/sbin/dlstat',
        '-p', '-o', 'zone,link,rbytes,obytes', '-T', 'u', str(period)]

    return  = cmdreader.get_stream(cmd, period)
