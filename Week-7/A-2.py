n=int(input())
x = [[0 for i in range(n)] for j in range(n)]
y= [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    p=list(map(int,input().split(" ",n)))
    for j in range(n):
        x[i][j]=p[j]
for i in range(n):
    for j in range(n):
        y[i][j]=x[j][i]
flag=0
for i in range(n):
    for j in range(n):
        if x[i][j]!=y[i][j]:
            flag=1
    if flag==1:
        break
if flag==1:
    print("NO")
else:
    print("YES")
