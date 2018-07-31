import re
import os

pat = r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)'
with os.popen('tasklist /nh', 'r') as f: # '/nh去掉进程池PID的表格头'
    for eachLine in f:
        print re.findall(pat, eachLine.rstrip())
f.close()