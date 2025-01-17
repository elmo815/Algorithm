N, M = map(int, input().split())

Nset = set() 
Mset = set() 
for _ in range(N):
    Nset.add(input())
for _ in range(M):
    Mset.add(input())

A = sorted(list(Nset & Mset))  

print(len(A))
for i in A:
    print(i)