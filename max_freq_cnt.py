T = int(input())

for test_case in range(1, T + 1):
    tc=int(input()) #tc 번호
    total=[]
    for score in range(101):
        total.append([0,score])

    in_score=list(map(int,input().split()))

    for i in range(1000):
        total[in_score[i]][0]+=1
    answer_1=max(total)
    answer_2=answer_1[1]
    print("#{} {}".format(test_case,answer_2))