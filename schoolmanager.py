
with open('D:\\leejh\\PycharmProjects\\jump\\schoolmanager.txt', 'r', encoding = "utf-8") as f:
    list = []
    data = f.read() # 파일 읽어오기
    list = data.split(',') # 문자열을 리스트로 변환
    list_1 = []
    for i in range(len(list)): # 2차원 리스트로 가공 [['손', 10, 20, 50], ['케인', 30, 40, 10]]
       if i %4 == 0:
           list_1.append([list[i],int(list[i+1]), int(list[i+2]), int(list[i+3])]) #list_1 = [['손', 10, 20, 50], ['케인', 30, 40, 10], ['알리', 20, 70, 30], [' 무리뉴', 50, 60, 70]]


    temp = []
    for j in range(len(list_1)):
        temp.append(round((list_1[j][1]+ list_1[j][2] +list_1[j][3])/3,2)) #과목수 만큼 나누기

        # temp = [26.67, 26.67, 40.0, 60.0]
    for a in range(len(list_1)):
        print("{}의 국영수 평균 점수 : {}".format(list_1[a][0], temp[a])) # 각 학생의 평균 점수 출력
