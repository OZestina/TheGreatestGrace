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

# =====================================================================================

# 1. 사용자의 입력값 중 숫자만 골라내 그래프를 그려주는 프로그램을 만드세요.
# 예시) 입력>> dig6aa2346dc103bbb05
# 출력)
# *       *
# *       *         *
# *     * *         *
# *   * * *     *   *
# * * * * *     *   *
# * * * * * *   *   *
# 6 2 3 4 6 1 0 3 0 5

st = input("입력>> ")
a = list()
for i in range(len(st)):
    #ASCII 코드로 해봄
    if 48 <= ord(st[i]) and ord(st[i]) <= 57 :
        a.append(int(st[i]))
        
# filter를 사용해 더 간결한 방법        
# numbers = list(filter(lambda x: x.isdecimal(), input('입력>> ')))
        
for i in range(max(a)):
    for j in range(len(a)):
        if int(a[j])-max(a)+i > -1 :
            print("* ", end="")
        else:
            print("  ", end="")
    print()
for i in range(len(a)):
    print(str(a[i])+" ", end="")


# 2.셀프넘버 합 구하기
# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# 예를 들어 d(91) = 9 + 1 + 91 = 101
# 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# 그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.

def d(n):
    result = n
    for i in range(len(str(n))):
        result += int(str(n)[i])
    return result
# d(n)을 한 줄로도 만들어봤다
# dd = lambda x: x + sum(map(int,list(str(x))))

# 5000개의 0으로 채워진 배열에 생성된 d(n)값을 카운트 
listA = [0 for i in range(5000)]
for i in range(5000):
    if d(i) < 5000:
        listA[d(i)] += 1

sum = 0
for i in range(len(listA)):
    if listA[i] == 0:
        #리스트 출력
        print(str(i), end=" ")
        #합 구하기
        sum += i
print()
print(sum)

#근데 이럴 것 없이 엄청 간단한 방법으로 한 줄 코딩이 가능했으니...
#iterate로 반환되는 것을 {}, []로 묶으면 바로 세트, 리스트로 변환 가능
#set는 중복없음, 교집합-합집합-차집합 연산 가능
#sum(iterate) 하면 다 더해서 돌려줌 (굳이 reduce를 쓸 필요가 없었네...)
#for문의 연산이 1줄로 가능할 경우 => 함수 for i in (iterate) 로 간편하게 사용 가능
a = sum(set(range(1,5000)) - {x + sum(int(i) for i in str(x)) for x in range(1,5000)})
print(a)
