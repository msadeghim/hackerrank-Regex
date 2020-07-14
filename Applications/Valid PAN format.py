import re
for x in range(int(input())):
     if re.match('^[A-Z]{5}[0-9]{4}[A-Z]$',input()):
         print('YES')
     else:
         print('NO')
