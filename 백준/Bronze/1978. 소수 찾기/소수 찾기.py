N = int(input())   

count = 0

number = map(int, input().split()) 

for i in number:         
    if i > 1 :          
        for j in range(2, i): 
            if i % j == 0:   
                break
        else:
            count += 1 

print(count)