
from visidata import *
from time import gmtime, strftime

@VisiData.api
def open_timeline(vd, p):
    return TimelineSheet(p.name, source=p)

class TimelineSheet(SequenceSheet):
    _rowtype = list  # rowdef: [str, str, str, str, str, str]

    def iterload(self):
        'Convert from MAC timeline.'
        yield(['Timestamp', 'Type', 'Mode', 'User', 'Group', 'File Name'])
        for line in self.source:
            (m, a, c, mode, user, group, name) = line.split(' ', 6)
            m = strftime('%Y-%m-%dT%H:%M:%S %Z', gmtime(float(m)))
            a = strftime('%Y-%m-%dT%H:%M:%S %Z', gmtime(float(a)))
            c = strftime('%Y-%m-%dT%H:%M:%S %Z', gmtime(float(c)))
            if m == a:
                if m == c:
                    yield([m, 'mac', mode, user, group, name])
                else:
                    yield([m, 'ma-', mode, user, group, name])
                    yield([c, '--c', mode, user, group, name])
            else:
                if m == c:
                    yield([m, 'm-c', mode, user, group, name])
                    yield([a, '-a-', mode, user, group, name])
                else:
                    yield([m, 'm--', mode, user, group, name])
                    if a == c:
                        yield([a, '-ac', mode, user, group, name])
                    else:
                        yield([a, '-a-', mode, user, group, name])
                        yield([c, '--c', mode, user, group, name])
