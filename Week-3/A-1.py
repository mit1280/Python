X = list(map(int, input().split(" "))) 
for i in range(len(X)):
  for j in range(0,len(X)-i-1):
    if X[j]>X[j+1]:
      X[j],X[j+1]=X[j+1],X[j]
      
print(X[len(X)-1],X[0])
