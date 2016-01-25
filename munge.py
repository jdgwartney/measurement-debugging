#!/usr/bin/env python

import petl as etl
from datetime import datetime

pulse_tab = (
    etl
    .fromcsv('measurements.csv')
    .convert('value', float)
    .convert('value', int)
    .convert('timestamp', int)
    .convert('timestamp', lambda t: datetime.fromtimestamp(int(t/1000.0)))
)
print(pulse_tab.lookall())

src_tab = (
    etl
    .fromjson('monitor.json', header=['timestamp', 'metric', 'source', 'measure'])
    .convert('timestamp', lambda t: datetime.fromtimestamp(int(t/1000.0)))
    .select('source', lambda v: v == 'panama-scheduler')
    .rename('measure', 'value')
)
print(src_tab.lookall())
