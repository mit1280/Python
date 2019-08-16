Given a list A of numbers, you have to print those numbers which are not multiples of 3.

Input Format:

The first line contains the numbers of list A separated by a space.

Output Format:

Print the numbers in a single line separated by a space which are not multiples of 3.

Example:

Input:

1 2 3 4 5 6 5

Output:

1 2 4 5 5

#code

X = list(map(int, input().split(" "))) 
Y=list()
for i in range(len(X)):
    if X[i]%3!=0:
      Y.append(X[i])
      
for i in range(len(Y)):
  print(Y[i],sep=' ',end=' ')
