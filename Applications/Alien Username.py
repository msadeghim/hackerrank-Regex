import re
 
pat = r'^[._]\d+[a-zA-Z]*_?$'
for i in range(int(input())):
    text = input()
    if re.search(pat, text):
        print('VALID')
    else:
        print('INVALID')
