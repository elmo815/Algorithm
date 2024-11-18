import sys

while(1):

    n=int(sys.stdin.readline())

    if n==0:
        break

    ch=[]

    for i in range(n):

        ch.append(input())

    ch.sort(key=str.lower)

    print(ch[0])