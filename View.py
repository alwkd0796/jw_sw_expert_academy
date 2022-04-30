for test_case in range(1,11):
    build_num=int(input())  #빌딩 수
    arr_build=list(map(int, input().split()))   #빌딩 높이 리스트 // 맨 앞과 맨 뒤 2개씩 빌딩 x(높이 0)
    cnt=0   #조망권 확보 가구 수
    for cur_pos in range(2,build_num-2):
        temp = 0
        if arr_build[cur_pos]==0: #빌딩이 없으면 넘기기
            continue
        else:   #빌딩이 있으면
            if arr_build[cur_pos-1]<arr_build[cur_pos] and arr_build[cur_pos]>arr_build[cur_pos+1]:    #현 위치 빌딩이 앞 뒤 빌딩보다 높을 경우
                if arr_build[cur_pos-2]<arr_build[cur_pos] and arr_build[cur_pos]>arr_build[cur_pos+2]:    #현 위치 빌딩이 -2, +2 빌딩보다 높을 경우
                    temp=max(arr_build[cur_pos-2],arr_build[cur_pos-1],arr_build[cur_pos+1],arr_build[cur_pos+2])
                    cnt+=arr_build[cur_pos]-temp
    print("#{} {}".format(test_case,cnt))