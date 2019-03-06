X = int(input()) 
Y=list()
a=0
if X==0:
  a=a+1
while X>0:
    p=int(X%10)
    Y.append(p)
    X=int(X/10)

b=0
p=0
for i in range(len(Y)):
    if Y[i]==0:
        a=a+1
    elif Y[i]==1:
        b=b+1
    else:
        p=1
if (a==1 or b==1) and p==0:
    print("YES")
else:
    print("NO")
