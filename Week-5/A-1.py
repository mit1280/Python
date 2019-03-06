X = list(map(int, input().split(" "))) 
t1=(X[0]*(2**0.5))/X[1]
t2=(2*X[0])/X[2]
if t1<t2:
    print("Walk")
else:
    print("Cab")
