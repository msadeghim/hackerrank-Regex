import sys
import re
 
lines = []
for line in sys.stdin:
    lines.append(line)
 
lines = ''.join(lines)
# print(lines)
 
res = re.findall(r'((//.*?)\n)|(/\*\*?.*?\*\*?/)', lines, re.DOTALL)
for ans in res:
    if ans[1] != '':
        k = ans[1].split('\n')
        for x in k:
            print(x.strip())
    else:
        k = ans[2].split('\n')
        for x in k:
            print(x.strip())
 
