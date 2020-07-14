attamp1
import re
for i in range(int(input())):
    text = input()
    if (bool(re.match(r'^[Hh][Ii]\s[^Dd]', text))):
        print(text)
 
Attemp2
import re
for i in range(int(input())):
    text = input()
    if re.match(r'^[Hh][Ii]\s[^Dd]', text):
        print(text)
 
