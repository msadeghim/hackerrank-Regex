import re
 
x = int(input())
lines = [input() for i in range(x)]
text = ' '.join(lines)
 
for x in range(int(input())):
    ans = 0
    a = input()
    b = a.replace('ze', 'se')
    ans += len(re.findall(r'\b' + a + r'\b', text))
    ans += len(re.findall(r'\b' + b + r'\b', text))
    print(ans)
