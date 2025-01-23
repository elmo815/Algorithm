n = int(input())
h = 0

for i in range(1, n+1): 
    nn = list(map(int, str(i)))  
    if i < 100:
        h += 1 
    elif nn[0]-nn[1] == nn[1]-nn[2]:
        h += 1 
print(h)