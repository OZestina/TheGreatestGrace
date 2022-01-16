# https://level.goorm.io/exam/49106/%EB%91%90%EB%B6%80-%EC%9E%90%EB%A5%B4%EA%B8%B0/quiz/1

# 중복된 결과 사전 차단을 위해 n을 set에 저장
# for문을 input의 절반만 돌아가게 처리하고 (n==2까지만 처리하도록)
# n==1인 경우를 포함하기 위해 마지막에 +1해서 리턴(출력)
user_input = int(input())
result = set()
for i in range(1, user_input//2 + 1):
	result.add(user_input // i)
print(len(result)+1)
