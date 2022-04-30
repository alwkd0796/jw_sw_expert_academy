T = int(input())

for test_case in range(1, T + 1):
    N=int(input())   #영역 개수
    a = [['']*10 for _ in range(10)]
    cnt=0
    for i in range(N):
        x1, y1, x2, y2, color=map(int, input().split())
        for j in range(x1, x2+1):
            for k in range(y1, y2+1):
                if color == 1:  #빨강
                    a[j][k]+='R'
                elif color == 2:    #파랑
                    a[j][k]+='B'
    for i in range(10):
        for j in range(10):
            if 'R' in a[i][j] and 'B' in a[i][j]:
                cnt+=1
    print('#{} {}'.format(test_case,cnt))