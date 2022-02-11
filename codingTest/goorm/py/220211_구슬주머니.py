# https://level.goorm.io/exam/49102/%EA%B5%AC%EC%8A%AC-%EC%A3%BC%EB%A8%B8%EB%8B%88/quiz/1

# 1st try
# 8, 11, 12 실패 (Timeout) => 메모리를 더 쓰면서 연산시간을 더 줄이는 방법이 있을까

# input 값 처리
user_input = int(input())
marbles = [int(x) for x in input().split()]

# 연산에 필요한 변수, 리스트 생성
count = 0
result = []
number = []

#
for i in range(user_input):
	if marbles[i] in number:
		result.append(i)
		count += 1
		continue
	new = marbles.copy()
	new.pop(i)
	if max(new) * 2 == sum(new):
		result.append(i)
		count += 1
		number.append(marbles[i])
		
# 출력
print(count)
for i in result:
	print(i+1, end=' ')
