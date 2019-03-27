import re
def NumberFromStrings(string):
    numberfromstring = re.findall('\d+',string)
    return numberfromstring
 
text = input()
p=NumberFromStrings(text)
m=int(p[0])
for i in range(1,len(p)):
    if int(p[i])>m:
        m=int(p[i])
print(m)
