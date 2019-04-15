p=['A','B','B','D','O','P','Q', 'R', 'a','b','d','e', 'g', 'o', 'p', 'q']
x=input()
sum=0
for i in range(len(p)):
    sum=sum+int(x.count(p[i]))
print(sum)
