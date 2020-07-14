import re
cls = '[_0-9a-zA-Z]'
 
text = [input() for x in range(int(input()))]
text = '\n'.join(text)
for i in range(int(input())):
    word = input()
    pat = rf'\b{word}\b'
    print(len(re.findall(pat, text)))
