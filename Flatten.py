for test_case in range(1,11):
    d_cnt=int(input())  #덤프 횟수
    b_hei=list(map(int, input().split()))   #상자 높이 배열

    answer=0
    for i in range(d_cnt):
        if max(b_hei)-min(b_hei)<=1:    #최고 최소 높이 차 1 이하인 경우 종료
            break
        temp=0
        b_hei_M=max(b_hei)
        b_hei_m=min(b_hei)
        for j in range(len(b_hei)):
            if b_hei[j]==b_hei_M:
                b_hei[j]-=1
                temp=1  #최대값 수행 완료
                break
        if temp==1: #최대값 수행 완료 시 최소값 수행 시작
            for k in range(len(b_hei)):
                if b_hei[k]==b_hei_m:
                    b_hei[k]+=1
                    break
        answer=max(b_hei)-min(b_hei)
    print("#{} {}".format(test_case,answer))