n=int(input())
s=[]

for i in range(n):
  s.append(input().split())

s.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in s:
  print(j[0])