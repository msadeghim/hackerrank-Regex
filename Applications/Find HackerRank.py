Attemp1
import re
for x in range(int(input())):
     text = input()
     if re.search(r'^hackerrank.*hackerrank$', text) or text == 'hackerrank':
         print(0)
     elif re.search(r'^hackerrank', text):
         print(1)
     elif re.search(r'hackerrank$', text):
         print(2)
     else:
         print(-1)
Attemp2
import re
for x in range(int(input())):
     text = input()
     start = re.search(r'^hackerrank',text)
     end = re.search(r'hackerrank$',text)
     if start and end:
         print(0)
     elif start:
         print(1)
     elif end:
         print(2)
     else:
         print(-1)
 
