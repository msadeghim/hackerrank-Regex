Regex_Pattern = r"\d\d\D\d\d\D\d{4}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
