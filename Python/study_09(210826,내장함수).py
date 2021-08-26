# 출제문제 - 1줄로 코딩하기

# 입력 리스트: [1,-5,3,-4,2,-3,0,-2,-1]
# 1) 리스트의 각 항목에 3을 더해서 리스트로 출력해보세요
# 출력:[4, -2, 6, -1, 5, 0, 3, 1, 2]
print(list(map(lambda a:a+3,[1,-5,3,-4,2,-3,0,-2,-1])))

# 2) 리스트의 각 항목 중 0보다 큰 항목만 리스트로 출력해보세요
# 출력:[1, 3, 2]
print(list(filter(lambda x: x>0,[1,-5,3,-4,2,-3,0,-2,-1])))

# 3) 리스트를 정렬하여 출력해보세요
# 출력: [-5, -4, -3, -2, -1, 0, 1, 2, 3]
print(sorted([1,-5,3,-4,2,-3,0,-2,-1]))

# 1+2+3) 하기 리스트의 각 항목에 3을 더해서 0보다 큰 항목만 리스트로 정렬하여 출력해보세요
# 출력: [1, 2, 3, 4, 5, 6]
print(sorted(filter(lambda x: x>0,map(lambda a:a+3,[1,-5,3,-4,2,-3,0,-2,-1]))))

# =====================================================================================

# 1. "textfile.txt"의 파일명으로 "글자를 파일에 쓰세요"라고 저장하고,
# 발생할 수 있는 IOError를 예외처리 후에 "파일을 찾을 수 없습니다."라고 출력하시오.
# 만약 예외가 발생하지 않는다면 "파일을 생성했습니다." 라고 출력하시오.
try:
    f = open("textfile.txt", 'w')
    f.write("글자를 파일에 쓰세요")
except IOError:
    print("파일을 찾을 수 없습니다.")
finally:
    print("파일을 생성했습니다.")

# 2. 가위바위보 게임 만들기
# random 모듈을 사용해 베타고라는 가위바위보 게임을 만들어 보세요.

# 랜덤넘버 생성
import random
a = random.choice(["가위","바위","보"])

# 가위바위보 인풋값 받기
b = input("가위, 바위, 보! >>")
# 승자 계산
if b == "가위":
    if a == "바위":
        print("컴퓨터는 '바위' 선택")
        print("졌습니다ㅠㅠ")
    elif a == "가위":
        print("컴퓨터는 '가위' 선택")
        print("비겼습니다")
    else:
        print("컴퓨터는 '보' 선택")
        print("이겼어요^^")
elif b == "바위":
    if a == "바위":
        print("컴퓨터는 '바위' 선택")
        print("비겼습니다")
    elif a == "가위":
        print("컴퓨터는 '가위' 선택")
        print("이겼어요^^")
    else:
        print("컴퓨터는 '보' 선택")
        print("졌습니다ㅠㅠ")
elif b == "보":
    if a == "바위":
        print("컴퓨터는 '바위' 선택")
        print("이겼어요^^")
    elif a == "가위":
        print("컴퓨터는 '가위' 선택")
        print("졌습니다ㅠㅠ")
    else:
        print("컴퓨터는 '보' 선택")
        print("비겼습니다")
else:
    print("가위, 바위, 보 만 입력해주세요")

# 3. 리스트넣어서 랜덤추첨하는 함수 만들기 (중복x)
import random
def ran(lists, n):
    setList = set()
    while True:
        a = random.randint(0, len(lists)-1)
        setList.add(member[a])
        if len(setList) == n:
            break
    return list(setList)

member = ["이준규", "변승원", "오주현", "전혜윤"]
print(ran(member, 2)) #['변승원', '전혜윤']


# 4. 계산기 만들기 , 나누기0 입력시 예외처리(ZeroDivisionError)
class Calculator:
    def __init__(self):
        self.result = 0
    def plus(self, x):
        self.result += x
    def minus(self, x):
        self.result -= x
    def mul(self, x):
        self.result *= x
    def div(self, x):
        try:
            self.result /= x
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다")

a = Calculator()
a.plus(3)
a.div(0)
# print(a.result)


# 5. lambda와 filter를 이용하여
# ['paper', 'sunflower', 'ketchup', 'mustard', 'pen', 'hamburger', 'spoon', 'couch']
# 리스트에서 a가 들어간 단어만 찾아보세요

lists = ['paper', 'sunflower', 'ketchup', 'mustard', 'pen', 'hamburger', 'spoon', 'couch']
print(list(filter(lambda x: 'a' in x,lists)))


# 6. 시험 성적표를 받은 당신, 한 과목이라도 50점 미만이면 회초리가 기다리고 있다
# lambda와 map으로 성적을 위조하여 부모님에게 칭찬을 받아 보자
# (당신의 과목당 점수는 random 모듈을 사용하여 생성하자)
# 예시: random신이 점지해주신 당신의 점수 [1, 62, 9, 31, 67, 93]
# 조작 후 점수: [51, 62, 59, 81, 67, 93]

print(list(map(lambda x: 50+x if x <50 else x,[1, 62, 9, 31, 67, 93])))
