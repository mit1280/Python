N = int(input())

List = list()
for i in range(N):
  List.append(int(input()))
List.sort()

print(*List,end="")
