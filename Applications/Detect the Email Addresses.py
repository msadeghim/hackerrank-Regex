import re
 
text = [input() for x in range(int(input()))]
text = '\n'.join(text)
ls = re.findall(rf'(\w+(\.\w+)*\@\w+(\.[a-z]+)+)', text)
ls = list(set([i[0] for i in ls]))
ls.sort()
print(';'.join(ls))
 
Attepmt2
import re
text = [input() for x in range(int(input()))]
text = '\n'.join(text)
print(';'.join(sorted(set(re.findall(r'\w+[\w.]+@[\w.]+\w+', text)))))
 
 
simpler: regex = re.compile(r'(\w[\w.]*@[\w.]*\w)')
emailPattern = re.compile('[\w\.]+@[\w\.]+[\w]+')
 
Note: sorted(ls)
