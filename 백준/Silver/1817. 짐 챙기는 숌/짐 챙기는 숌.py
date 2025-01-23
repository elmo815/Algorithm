n, m=map(int,input().split())
box=0

if n==0: 
  print(0)
else:
  books=list(map(int,input().split()))
  w=0
  box=1
  for i in books:
    if i+w <= m:
      w += i
    else:
      w = i
      box += 1
  print(box)