import re
a = 0
for i in range(int(input())):
    if re.search(r'hackerrank',input().lower()):
        a+=1
print(a)
