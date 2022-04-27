T = int(input())

for test_case in range(1, T + 1):
    str1=input()    # 길이가 N인 문자열 입력
    str2=input()    # 길이가 M인 문자열 입력

    #입력받은 두 개의 문자열을 문자 한 개씩 리스트로 저장
    arr_str1=[]
    arr_str2=[]
    for i in str(str1):
        arr_str1.append(i)
    for j in str(str2):
        arr_str2.append(j)

    sub_len=len(str2)-len(str1)

    answer=0
    cnt_p=0
    for l in range(sub_len+1):  #str1위치가 str2 주소 첫번째부터 우측으로 이동
        cnt = 0
        for k in range(len(str1)):  #str1 문자들을 str2 정해진 주소에 있는 문자들과 비교
            if arr_str1[k]==arr_str2[l+k]:  #str1의 첫 번째 문자와 str2 첫 번째 문자 비교
                cnt+=1
                if cnt==len(str1):
                    break
            else:
                break
        if cnt==len(str1):
            answer=1
            break

        cnt_p+=1

    print('#{} {}'.format(test_case,answer))