import re
import os
with os.popen('whodata.txt', 'r') as f:
    for eachLine in f:
        print re.split(r'\s\s+|\t', eachLine.rstrip())
f.close()