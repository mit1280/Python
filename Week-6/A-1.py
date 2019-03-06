n=int(input())
X = list(map(int, input().split(" ",n))) 
p=int(input())
p=p-1
x1=X[p]
X.sort()
print(X.index(x1)+1)
