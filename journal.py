
from visidata import *

@VisiData.api
def open_journal(vd, p):
    return JournalSheet(p.name, source=p)

class JournalSheet(SequenceSheet):
    _rowtype = list  # rowdef: [str, str, str, str]

    def iterload(self):
        'Convert from journal files.'
        yield(['Timestamp', 'Hostname', 'Facility', 'Message'])
        for line in self.source:
            if not line.startswith('-- '):
                timestamp = line[0:15]
                (hostname, facility, message) = line[16:].split(' ', 2)
                yield([timestamp, hostname, facility[:-1], message])
