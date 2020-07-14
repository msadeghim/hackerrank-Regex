Attemp1
import re
for i in range(int(input())):
    text = input()
    match = re.findall(r'\d+', text)
    print('CountryCode='+match[0]+','+'LocalAreaCode='+ match[1]+','+'Number='+ match[2])
