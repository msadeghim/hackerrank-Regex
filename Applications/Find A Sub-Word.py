Attemp 1
import re
 
regex_pattern = r"\w+"  # Do not delete 'r'.
 
line_list = []
lines = int(input())
 
for i in range(0, lines):
    line_list.append(input())
 
 
queries = int(input())
 
for i in range(0, queries):
    rg = r'\w' + input() + r'\w'
    ans = 0
    for x in range(0, lines):
        match = re.findall(regex_pattern, line_list[x])
 
        for s in match:
            ans = ans + len(re.findall(rg, s))
 
    print(ans)
 
Attemp2
import re
 
lines = int(input())
line_list = [input() for i in range(lines)]
queries = int(input())
 
for i in range(0, queries):
    rg = r'\w' + input() + r'\w'
    ans = 0
    for x in range(0, lines):
        ans += len(re.findall(rg, line_list[x]))
    print(ans)
 
Attemp3
import re
 
line_list = [input() for i in range(int(input()))]
string = ';'.join(line_list)
 
for i in range(0, int(input())):
    print(len(re.findall(r'\w' + input() + r'\w', string)))
 
