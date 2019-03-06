X = list(map(int, input().split(" "))) 
y=[0]*len(X)
for i in range(len(X)):
    y[i]=X[i]
X.sort()


j=0
while(j<len(X)):
    if y[j]==X[j]:
        j+=1
    else:
        break
if j>0:
    if j==len(X):
        print("0")
    else:
        print(len(X)-j-1)
else:
    j=0
    k=1
    while(k<len(X)):
        if y[k]==X[j]:
            j+=1
        k+=1
    print(len(X)-j)
