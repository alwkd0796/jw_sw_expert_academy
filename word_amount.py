T = int(input())

for test_case in range(1, T + 1):
    str1=input()
    str2=input()    #문자열 str1, str2 입력

    #문자열 str1에 포함된 문자들이 str2에 몇 개씩 있는지 찾기

    #str1에서 첫 번째 원소를 새로운 리스트(a)에 저장.
    #str1 두 번째 원소를 이전 원소와 비교하여 다르다면 리스트(a)에 저장(a.append), 같다면 continue
    a = []  # str1 에서 중복 제거한 문자열 리스트
    a.append(str1[0])

    b=[0]*1000    # 글자 갯수 저장 리스트
    m_cnt=0
    for i in range(1,len(str1)):
        n_cnt = 0
        cnt = 0
        for j in range(len(a)):
            if str1[i]==a[j]:
                n_cnt+=1
            else:
                cnt+=1
        if (n_cnt+cnt==len(a)) and n_cnt==0:  # 다음 문자가 len(a) 만큼 반복해서 리스트 a에 저장된 같은 문자가 없다면 저장.
            a.append(str1[i])
    #print(a) #확인용, a 정상 출력됨

    for k in range(len(str2)):
        for l in range(len(a)):
            if str2[k]==a[l]:
                b[l]+=1
            else:
                continue
    m_cnt=max(b)
    print("#{} {}".format(test_case, m_cnt))