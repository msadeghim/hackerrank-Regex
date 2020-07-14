import re
 
a = int(input())
ans = []
for _ in range(a):
    s = input()
    res = re.findall(r'https?://(www2?\.)?(([A-Za-z0-9-]+\.)+[A-Za-z0-9]+)', s)
 
    for t in res:
        if t[1]:
            ans.append(t[1])
 
 
print(';'.join(sorted(list(set(ans)))))
