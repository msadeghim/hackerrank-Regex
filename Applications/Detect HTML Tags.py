میگه تگ نیم ها رو دربیاریم. تکراری هاشو حذف کنیم و مرتب شده با سمی کلن سپریتت نشون بدیم.
مسخرس
کافیه فقط بخش ابتدا(باز) تگ رو بررسی کنیم
و بسته شدنش نیاز نیست چک بشه
حتی اینم جواب میده
reg = r'<(\w+)'
 
 
import re
 
reg = r'< *(\w+).*?>'
 
a = int(input())
ls = []
for i in range(a):
    f = re.findall(reg, input())
    for j in f:
        ls.append(j)
 
print(';'.join(sorted(list(set(ls)))))
 
import re, sys
print(';'.join(sorted(set(re.findall('<(\w+)', sys.stdin.read())))))
