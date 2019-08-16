Given a list of numbers, find maximum and minimum in this list.

Input Format:

The first line contains numbers separated by a space.

Output Format:

Print maximum and minimum separated by a space

Example:

Input:

1 2 3 4 5

Output:

5 1

#code

X = list(map(int, input().split(" "))) 
for i in range(len(X)):
  for j in range(0,len(X)-i-1):
    if X[j]>X[j+1]:
      X[j],X[j+1]=X[j+1],X[j]
      
print(X[len(X)-1],X[0])
