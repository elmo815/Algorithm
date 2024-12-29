dic={'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
dial=input()
time=0
for i in range(len(dial)):
  for k in dic.keys():
    if dial[i] in k:
      time+=dic[k]
print(time)