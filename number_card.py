"""
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )
"""

T = int(input())    #TC 입력

for test_case in range(1, T + 1):
    N=int(input())  #카드 장수 입력
    No=int(input()) #카드 숫자들 입력

    list_str=[]
    for i in str(No):
        list_str.append(i)  #숫자들 list에 개별 저장

    list_int=list(map(int, list_str))   #list 저장된 각 원소들 int형변환

    #많은 개수의 숫자 찾기

    #0~9까지 숫자의 개수를 저장할 2차원 배열 생성
    cnt=[]
    for j in range(10):
        cnt.append([0,j])

    for k in range(len(list_int)): #list_int 각 원소를 탐색하며 어떤 숫자가 있는지 확인
        if list_int[k]==0:  #확인 된 숫자에 해당하는 cnt 원소 카운트
            cnt[0][0]+=1
        elif list_int[k]==1:
            cnt[1][0]+=1
        elif list_int[k] == 2:
            cnt[2][0] += 1
        elif list_int[k] == 3:
            cnt[3][0] += 1
        elif list_int[k] == 4:
            cnt[4][0] += 1
        elif list_int[k] == 5:
            cnt[5][0] += 1
        elif list_int[k] == 6:
            cnt[6][0] += 1
        elif list_int[k] == 7:
            cnt[7][0] += 1
        elif list_int[k] == 8:
            cnt[8][0] += 1
        elif list_int[k] == 9:
            cnt[9][0] += 1

    #print(cnt) cnt 확인
    #print(max(cnt)) max값 확인
    
    #1안 m_cnt=max(cnt)  #m_cnt는 [x,x] 리스트를 가짐
    
    #2안
    m_cnt=cnt[0]
    for l in range(1,len(cnt)):    # 가장 많은 수의 숫자 탐색
        if m_cnt[0]>cnt[l][0]:
            continue
        elif m_cnt[0]<cnt[l][0]:
            m_cnt=cnt[l]
        elif m_cnt[0]==cnt[l][0]:
            if m_cnt[1] > cnt[l][1]:    #가장 많은 수의 숫자가 여러개 일경우 큰 숫자를 탐색
                continue
            elif m_cnt[1] < cnt[l][1]:
                m_cnt = cnt[l]

    print('#{} {} {}'.format(test_case, m_cnt[1], m_cnt[0]))

        #카운트가 끝났을 때 cnt 2차원 배열 중 각 원소의 첫번째 원소가 max인 원소 탐색
        #그 원소의 첫번째 원소(숫자의 개수)와 두번째 원소 출력(가장 많은 개수의 숫자)



    #max_cnt(가장 많은 개수의 수), list.count(max_cnt)