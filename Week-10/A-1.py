import re
X=input()
r=re.compile('[@_!#$%^&*()<>?/\|{}~:;]')
if r.search(X)== None:
    print("NO")
else:
    print("YES")
