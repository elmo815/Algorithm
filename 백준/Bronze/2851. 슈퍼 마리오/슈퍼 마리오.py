score=[]
A=0
x=0
for i in range(10):
  score.append(int(input()))

while x<=9 :
  A += score[x]

  if (A==100) : 
    break

  elif (A >100) :
    if A-100 <= 100-(A-score[x]):
      break
    else :
      A = A-score[x]
    break

  x += 1
print(A)