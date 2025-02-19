C = int(input())  #테스트 케이스 개수

for i in range(C):
    num = list(map(int, input().split())) #입력, 정수 리스트로 변환,
    avg = sum(num[1:])/num[0]   #num[1:]점수 리스트,num[0]은 학생 수
    count = 0
    for i in range(1, len(num)):
        if num[i] > avg:
            count += 1
            
    print('%.3f' % (count / num[0] * 100) + '%')
