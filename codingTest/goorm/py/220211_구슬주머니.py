# https://level.goorm.io/exam/49102/%EA%B5%AC%EC%8A%AC-%EC%A3%BC%EB%A8%B8%EB%8B%88/quiz/1

# 2nd try => 성공!
# input 값 처리
user_input = int(input())
marbles = [int(x) for x in input().split()]

# 연산에 필요한 변수, 리스트 생성
fbig = max(marbles)		#가장 큰 수
sbig = sorted(marbles)[-2]	#두번째로 큰 수
total = sum(marbles)		#구슬 모두 더한 값
numbers = list(set(marbles))	#중복없는 구슬 값
result = []			#좋은 주머니를 만드는 수 (뺐을 때 좋은 주머니를 만드는 구슬의 값)
answer = []			#제외할 구슬의 위치

# 연산1
for i in numbers:
	if i == fbig:
		if sbig * 2 == total - fbig:
			result.append(i)
	else: #제일 큰 수가 아닐 경우
		if fbig * 2 == total - i:
			result.append(i)
# 연산2
for i in range(user_input):
	if marbles[i] in result:
		answer.append(i)

# 출력
print(len(answer))
for i in answer:
	print(i+1, end=' ')
	
	
# =========================================================================
# 1st try
# 8, 11, 12 실패 (Timeout) => 메모리를 더 쓰면서 연산시간을 더 줄이는 방법이 있을까

# input 값 처리
user_input = int(input())
marbles = [int(x) for x in input().split()]

# 연산에 필요한 변수, 리스트 생성
result = []
number = []

# 연산
for i in range(user_input):
	if marbles[i] in number:
		result.append(i)
		continue
	new = marbles.copy()
	new.pop(i)
	if max(new) * 2 == sum(new):
		result.append(i)
		number.append(marbles[i])
		
# 출력
print(len(result))
for i in result:
	print(i+1, end=' ')
