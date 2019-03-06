X = list(map(int, input().split(" "))) 
Y=list()
for i in range(len(X)):
    if X[i]%3!=0:
      Y.append(X[i])
      
for i in range(len(Y)):
  print(Y[i],sep=' ',end=' ')
