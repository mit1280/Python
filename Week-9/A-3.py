p = input()
for i in range(len(p)):
    if p[i]=='@':
        j=i+1
        while(p[j]!='.'):
            print(p[j],end='')
            j=j+1
