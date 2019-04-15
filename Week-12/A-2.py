x=str(input())
l=[]
q=x.replace('.','a')
p=''.join(reversed(q))
if (p==q):
    print(p)
else:
    print(-1)
