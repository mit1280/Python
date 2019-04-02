c=50
h=30
X = list(map(int, input().split(",")))
for i in range(len(X)):
  q=(2*c*X[i]/h)**(1/2)
  if i<len(X)-1:
      print(round(q),end=',')
  else:
      print(round(q),end='')
