import re
for x in range(int(input())):
     text = input()
     regex = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}'
     if re.search(regex, text):
         print('VALID')
     else:
         print('INVALID')
