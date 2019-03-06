a,b= map(int,input().split())
for i in range(1,a*b+1):
    if(i%(b) == 0):
    	print(i,end="")
    	print("\n",end="")
    else:
    	print(i,end=" ")
