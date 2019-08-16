You all have seen how to write loops in python. Now is the time to implement what you have learned.

Given an array A of N numbers, you have to write a program which prints the sum of the elements of array A with the corresponding elements of the reverse of array A.
If array A has elements [1,2,3], then reverse of the array A will be [3,2,1] and the resultant array should be [4,4,4].

Input Format:

The first line of the input contains a number N representing the number of elements in array A.
The second line of the input contains N numbers separated by a space. (after the last elements, there is no space)

Output Format:

Print the resultant array elements separated by a space. (no space after the last element)

Example:

Input:
4
2 5 3 1

Output:
3 8 8 3

#code
x=int(input())
X = list(map(int, input().split(" ",x))) 
y=list()
for i in range(x):
    y.insert(i,int(X[x-i-1]+X[i]))
for i in range(x):
    print(y[i],sep=' ',end=" ")
