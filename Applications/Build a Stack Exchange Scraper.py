import sys, re
stack = sys.stdin.read()

results = re.findall(r'question-summary-(\d{5})".*?class="question-hyperlink">(.+?)</a>.*?class=\"relativetime\">(.+?)</span>', stack, re.DOTALL)

for result in results:
    print(';'.join(result))
