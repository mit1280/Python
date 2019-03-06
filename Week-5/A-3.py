def sePrime(n):
    x=[]
    while n!=1:
        for i in range(2,int(n+1)):
            a=n/i
            p=a-int(a)
            if p!=0 :
                continue
            else:
                x.append(i)
                n=a
                break
    f=0
    for i in range(len(x)):
        p=x.count(x[i])
        if p>1:
            f=1
    if f==0 and len(x)>1:
        return 1
    else:
        return 0

n=int(input())
c=n-2
d=2
flag=0
while c>d:
    x1=sePrime(c)
    x2=sePrime(d)
    if x1==1 and  x2==1:
        flag=1
        break
    c-=1
    d+=1

if flag==1:
    print("Yes")
else:
    print("No")
    
