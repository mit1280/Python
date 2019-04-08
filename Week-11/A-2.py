x=list(map(str,input().split(",")))
x.sort()
for i in range(len(x)):
  if(i<len(x)-1):
     print(x[i],end=",")
  else:
     print(x[i])
