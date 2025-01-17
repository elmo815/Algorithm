A = set(range(1, 10001)) 
B = set()

for i in A : #
    for n in str(i):
        i += int(n)
    B.add(i) 

C = A - B 
for C in sorted(C):  
    print(C)