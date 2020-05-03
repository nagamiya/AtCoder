import re
# input
n = input()
if (re.match('.*7.*', n)):
    print("Yes")
else:
    print("No")