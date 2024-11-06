price =int(input())
number =int(input()) 
sum= 0

for i in range(0, number):
    A, B = map(int, input().split())
    sum += A*B

if sum == price:
    print("Yes")
else:
    print("No")