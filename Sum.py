for test_case in range(1,11):
    tc=int(input())
    arr=[]
    arr_total=[]
    for i in range(100):
        arr.append(list(map(int,input().split())))  #2차원 배열 생성
    for i in range(100):
        ver_sum = 0
        hor_sum = 0
        dia_rb_sum = 0  # 대각 우하
        dia_ru_sum = 0  # 대각 우상
        for j in range(100):
            ver_sum+=arr[i][j]
            hor_sum+=arr[j][i]
            dia_rb_sum+=arr[j][j]
            dia_ru_sum+=arr[99-j][j]
        arr_total.append(ver_sum)
        arr_total.append(hor_sum)
        arr_total.append(dia_rb_sum)
        arr_total.append(dia_ru_sum)
    #print(arr_total)
    print("#{} {}".format(tc,max(arr_total)))