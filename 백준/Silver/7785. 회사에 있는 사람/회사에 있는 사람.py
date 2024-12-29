n=int(input())
dic={}
for i in range(n):
  name, geegle = map(str, input().split())
  if geegle == 'enter':
      dic[name] = geegle
  else :
     del dic[name]

dic = sorted(dic.keys(), reverse=True)
for j in dic:
    print(j)