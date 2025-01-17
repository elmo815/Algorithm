A = set(range(1, 10000))
B = set()  
for num in A :
    for n in str(num):
        num += int(n)
    B.add(num) 

C = A - B
for C in sorted(C): 
    print(C)