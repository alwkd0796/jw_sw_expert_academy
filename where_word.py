T = int(input())

for test_case in range(1, T + 1):
    N, K=map(int,input().split())  # N x N 크기, 단어의 길이 K
    arr=[]
    for i in range(N):
        arr.append(list(map(int,input().split())))

    answer=0
    #가로줄 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]==1:
                cnt+=1
            if arr[i][j]==0 or j==N-1:
                if cnt==K:
                    answer+=1
                cnt = 0
    #세로줄 탐색
        for j in range(N):
            if arr[j][i]==1:
                cnt+=1
            if arr[j][i]==0 or j==N-1:
                if cnt==K:
                    answer+=1
                cnt = 0

    print('#{} {}'.format(test_case,answer))