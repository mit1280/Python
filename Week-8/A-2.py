X = list(map(str,input()))
f=0
for i in range(0,26):
    x=X.count(chr(i+97))
    if(x==0):
        x=X.count(chr(i+65))
        if (x==0):
            f=1
            break
if f==1:
    print("NO")
else:
    print("YES")

