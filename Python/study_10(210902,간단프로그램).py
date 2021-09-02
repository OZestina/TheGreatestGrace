# 출제문제 - 간단한 타자연습 프로그램 만들기
#진행할 짧은 글 연습 개수를 입력받아, 해당하는 만큼의 연습을 진행하고
#정확도(소수점 없는 백분율)와 걸린시간(초)를 출력하는 프로그램(함수) typing_game을 만들어보세요
#연습 개수의 경우 사용자가 정수만 입력한다고 가정합니다
#연습 문장은 제시된 리스트에서 랜덤으로 나오도록 해주세요

import time
import random
sentences = ['String sql = "select * from member";',
             '@Controller',
             '@Autowired',
             '@RequestMapping()',
             '@Repository',
             'static SingleObject object;',
             'public static SingleObject getInstance()',
             'Connection con = DriverManager.getConnection(url, user, password);',
             'Class.forName("com.mysql.jdbc.Driver");',
             'PreparedStatement ps = con.prepareStatement(sql);']

def typing_game(n):
    score = 0
    total_length = 0
    start_time = time.time()

    for i in range(int(n)):
        random_sentence = sentences[random.choice(sentences)]
        print(random_sentence)
        sentence = input(">> ")
        total_length += len(random_sentence)
        if len(random_sentence) <= len(sentence):
            for i in range(len(random_sentence)):
                if random_sentence[i] == sentence[i]:
                    score += 1
        else:
            for i in range(len(sentence)):
                if random_sentence[i] == sentence[i]:
                    score += 1
    end_time = time.time()
    time_spend = end_time - start_time

    print("당신의 정확도는 "+str(score*100//total_length)+"%입니다.")
    print("걸린 시간은 총 "+str(round(time_spend))+"초입니다.")


print("타자연습에 오신 것을 환영합니다")
n = input("몇 줄의 짧은글 연습을 하시겠어요?(1 이상의 정수) >> ")
typing_game(n)
