A=list(map(int,input().split(" ")))
B=list(map(int,input().split(" ")))
B.sort()
i=1
min=B[A[1]-1]-B[0]
while((i+A[1])<len(B)):
    x=B[i+A[1]-1]-B[i]
    if min>x:
        min=x
    i+=1
print(min)
