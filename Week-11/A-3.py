x=list(map(int,input().split(" ")))
p=x.count(0)
for i in range(p):
    x.remove(0)
    x.append(0)
for i in range(len(x)):
  if(i<len(x)-1):
     print(x[i],end=" ")
  else:
     print(x[i])
