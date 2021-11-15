
from visidata import *

@VisiData.api
def open_log(vd, p):
    return LogSheet(p.name, source=p)

class LogSheet(SequenceSheet):
    _rowtype = list  # rowdef: [str, str, str, str]

    def iterload(self):
        'Convert from syslog files.'
        yield(['Timestamp', 'Hostname', 'Facility', 'Message'])
        for line in self.source:
            timestamp = line[0:15]
            (hostname, facility, message) = line[16:].split(' ', 2)
            yield([timestamp, hostname, facility[:-1], message])
