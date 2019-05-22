"""main class of log analyzer project"""
from os import walk
import os
import pprint
from glob import glob

PP = pprint.PrettyPrinter(indent=4)
RESULT = []

PATH = '\\\\cs-p-log1\\ProductionLogging\\2019-04\\Exceptions\\Services'
for x in walk(PATH):
    for y in glob(os.path.join(x[0], '*.txt')):
        RESULT.append(y)
PP.pprint(RESULT)

for f in RESULT:
    if 'converting' in open(f).read():
        PP.pprint(f)
