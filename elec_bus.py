T = int(input())

for test_case in range(1, T + 1):
    K,N,M=map(int,input().split())  #한 번에 갈 수 있는 정류장 수 K, 종점 N, 충전기가 설치된 정류장 수 M
    stop=list(map(int,input().split())) #충전기가 설치된 정류장

    current=0
    cnt=0

    while (current+K)<N:
        for i in range(K,0,-1):
            if (current+i) in stop:
                current+=i
                cnt+=1
                break
        else:
            cnt=0
            break

    print("#{} {}".format(test_case,cnt))