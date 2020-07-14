import re
 
a = int(input())
ans = {}
for i in range(a):
    s = input()
    res = re.findall(r'<(\w+)(.*?)>', s)
    for r in res:
        tag, att = r
        if tag not in ans.keys():
            ans[tag] = []
        at = re.findall(r'(\w+)=["\']', att)
        for x in at:
            ans[tag].append(x)
 
 
ans2 = sorted(ans)
for x in ans2:
    print(x+':'+','.join(sorted(set(ans[x]))))
