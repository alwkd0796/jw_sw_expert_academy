T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())    #NxN과 문자열 길이 M 입력

    arr_2 = []
    for l in range(N):
        arr_2.append(input())     # NxN 행렬 입력

    for i in range(N):
        for k in range(N-M+1):
            sent_h = []
            sent_v = []
            for j in range(M):
                sent_h+=arr_2[i][k+j] #가로 M개 문자 리스트화
                sent_v+=arr_2[j+k][i] #세로 M개 문자 리스트화
            if sent_h==sent_h[::-1]:
                answer=''.join(sent_h)
                break
            elif sent_v==sent_v[::-1]:
                answer = ''.join(sent_v)
                break
    print('#{} {}'.format(test_case, answer))