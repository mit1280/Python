n=int(input())
x = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    p=list(map(int,input().split(" ",n)))
    for j in range(n):
        x[i][j]=p[j]
for i in range(n):
    for j in range(n):
        if i<j:
            x[j][i]=0
for i in range(n):
    for j in range(n):
      if j==n-1:
        print(x[i][j],end='')
      else:
        print(x[i][j],end=' ')
    if i<n-1:
      print()
