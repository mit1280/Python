n=list(map(int,input().split(" ",2)))
x = [[0 for i in range(n[1])] for j in range(n[0])]
for i in range(n[0]):
    p=list(map(int,input().split(" ",n[1])))
    for j in range(n[1]):
        x[i][j]=p[j]
flag=0
for i in range(n[0]):
    for j in range(n[1]):
        if x[i][j]>1:
            flag=1
    if flag==1:
        break
if flag==1:
    print("NO")
else:
    print("YES")
