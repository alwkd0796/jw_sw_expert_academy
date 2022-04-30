for test_case in range(1, 11):
    tc=int(input())
    arr=[]
    for i in range(100):
        arr.append(list(map(int,input().split())))
    pause = 0
    for x in range(100):
        y = 0
        x_cur = 0
        answer = 0
        if arr[y][x]==1:  #목적지에 도착했다면 그 때 여기 x 위치 출력
            x_cur=x
            while 1:
                y += 1  # 좌 또는 우측에 1이 없을 경우 계속 내려감
                if arr[y][x_cur]==2:    #목적지 도착
                    pause=1
                    answer=x
                    break
                if y==99 and arr[y][x_cur]!=2:
                    break
                if y<99:
                    if 0<x_cur<99:
                        if arr[y][x_cur-1]==1:    #좌측에 1이 있을 경우
                            x_cur -= 1
                            while arr[y][x_cur-1]==1:
                                x_cur-=1
                                if x_cur == 0:
                                    break
                        elif arr[y][x_cur+1]==1:  #우측에 1이 있을 경우
                            x_cur+=1
                            while arr[y][x_cur+1]==1:
                                x_cur+=1
                                if x_cur == 99:
                                    break
                    elif x_cur==0:
                        if arr[y][x_cur+1]==1:  #우측에 1이 있을 경우
                            x_cur+=1
                            while arr[y][x_cur+1]==1:
                                x_cur+=1
                    elif x_cur==99:
                        if arr[y][x_cur-1]==1:    #좌측에 1이 있을 경우
                            x_cur-=1
                            while arr[y][x_cur-1]==1:
                                x_cur-=1
        if pause==1:
            break
    print("#{} {}".format(tc,answer))