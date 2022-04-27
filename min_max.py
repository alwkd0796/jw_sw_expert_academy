"""
while 1:
        T=int(input("테스트 케이스 수="))  #테스트 케이스 수 입력

        if 1<=T<=50:
            for test_case in range(1, T+1):
                N = int(input("양수의 개수="))   #각 케이스의 양수 개수 입력
                if 5 <= N <= 1000:
                    list=list(map(int, input().split()))
                    if 1 <= list[i] <= 1000000:
                        continue
                    else:
                        break
                #입력 받은 양수 비교
                while 1:
                    #list가 앞에서부터 큰 수로 정렬 되었을 때 while을 종료한다는 문장
                    num=0
                    for i in range(N):
                        if list[i+1]>list[i]:
                            num+=1
                    if num==N-1:
                        break

                    # 큰 순서대로 정렬
                    for i in range(N):
                        temp=list[i]
                        list[i]=temp if temp>=list[i+1] else list[i+1]   #비교해서 큰 수를 앞에, 작은 수를 뒤에 위치
                        if temp<list[i+1]:  #뒤에 수가 더 큰 수였다면, 앞 수를 뒤에 저장
                            list[i+1]=temp
                    else:
                        print("1과 1,000,000 사이의 정수로 입력해주세요")
                else:
                    print("5 <= N <= 1000 사이의 정수로 입력해주세요")

                output = list[N + 1] - list[0]  #가장 큰 수와 가장 작은 수 차
                print('#',T,' ',output)   #출력

                T -= 1
        else:
            print("1<=T<=50 사이의 정수로 입력해주세요")
"""

"""
T = int(input("테스트 케이스 수="))  # 테스트 케이스 수 입력
for test_case in range(1, T + 1):
    N = int(input("양수의 개수="))  # 각 케이스의 양수 개수 입력
    list = list(map(int, input().split()))

    
    # sort 해서 하는 법
    list.sort(reversed = True)
    # 5 6 7 8 9 -> 값
    # 0 1 2 3 4 -> index
    max = list[-1]
    min = list[0]
    answer = max - min
    

    # 배열 탐색해서 min, max 찾기
    min = list[0]
    max = list[0]
    for i in range(1, N):
        if min > list[i]:
            min = list[i]
        if max < list[i]:
            max = list[i]
    answer = max - min

    answer = max(list) - min(list)
"""

T = int(input())    #TC 입력
answer=[]

for test_case in range(1, T + 1):
    N = int(input())    #양수 개수 입력
    arr = list(map(int, input().split()))  #양수 입력
    answer.append(max(arr) - min(arr))

for cnt in range(T):
    cnt_2=cnt+1
    print('#{} {}'.format(cnt_2, answer[cnt]))