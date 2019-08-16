You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.

Input Format:

The first line contains a number made up of 0's and 1's.

Output Format:

Print 'YES' or 'NO' accordingly without quotes.

Example:

Input:

101

Output:
YES

#code

X = int(input()) 
Y=list()
a=0
if X==0:
  a=a+1
while X>0:
    p=int(X%10)
    Y.append(p)
    X=int(X/10)

b=0
p=0
for i in range(len(Y)):
    if Y[i]==0:
        a=a+1
    elif Y[i]==1:
        b=b+1
    else:
        p=1
if (a==1 or b==1) and p==0:
    print("YES")
else:
    print("NO")
