N = int(input())
A = []
while N != 1:
    for i in range(2, N + 1):
        if N % i == 0:
            A.append(i)
            N = N // i
            break

for i in A:
    print(i)