#N개의 정수를 리스트(a)로 받기
#리스트(a) 주소값을 +1하며 M개의 이웃한 원소 합을 다른 리스트(b)에 저장 시키기
#리스트(b)의 원소 중 max, min 값 도출하여 빼고 출력



T = int(input())    #TC 받기

for test_case in range(1, T + 1):
    N, M=map(int,input().split())  #입력 받을 정수 개수 N, 더할 이웃 원소 개수 M

    arr=list(map(int,input().split())) #N개 정수 입력 받아 리스트에 저장

    arr_sum=[]  #구간 합 저장시킬 리스트
    for i in range(N-M+1):  #이웃한 M개를 더할 수 있는 주소까지
        temp=0
        j=i
        for k in range(M):
            temp+=arr[j]
            j+=1

        arr_sum.append(temp)

    sub=max(arr_sum)-min(arr_sum)

    print("#{} {}".format(test_case, sub))