from os import walk
import os
import pprint
from glob import glob

pp = pprint.PrettyPrinter(indent=4)
result = []

PATH = '\\\\cs-p-log1\\ProductionLogging\\2019-04\\Exceptions\\Services'
for x in walk(PATH):
    for y in glob(os.path.join(x[0], '*.txt')):
        result.append(y)
pp.pprint(result)

for f in result:
    if 'converting' in open(f).read():
        pp.pprint(f)
