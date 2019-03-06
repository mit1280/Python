x=int(input())
X = list(map(int, input().split(" ",x))) 
y=list()
for i in range(x):
    y.insert(i,int(X[x-i-1]+X[i]))
for i in range(x):
    print(y[i],sep=' ',end=" ")
 

