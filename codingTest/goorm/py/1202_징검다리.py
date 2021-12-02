# https://level.goorm.io/exam/49112/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC-%EA%B1%B4%EB%84%88%EA%B8%B0/quiz/1

# 각 징검다리까지 도달하는 데 밟는 가장 적은 독을 별도의 배열로 저장하고 
# 마지막 3개의 징검다리 중 가장 적은 독을 가진 돌의 독을 리턴한다

#2nd try
def lessPoison(howLong, array):
	if howLong <= 2:
		return 0
	#초기값 세팅
	poison = [-1] * howLong
	poison[0:3] = array[0:3]
	#연산 시작
	for idx in range(howLong):
		current = poison[idx]
		for i in range(1,4):
			if idx + i < howLong:
				if poison[idx+i] == -1:
					poison[idx+i] = current + array[idx+i]
				elif poison[idx+i] > current + array[idx+i]:
					poison[idx+i] = current + array[idx+i]
	#연산후결과반환
	return min(poison[-3:])

howLong = int(input())
array = [int(x) for x in input().split()]

result = lessPoison(howLong, array)
print(result)

#================================================================

#1st try
#처음에 생각한건 queue로 검사할 idx를 저장하는 거였는데
#생각해보니 0~howLong까지 순차적으로 검사하는 거여서 없어도 됐다^^

from collections import deque

def lessPoison(howLong, array, poison):
	if howLong <= 2:
		return 0
	queue = deque()
	#초기값 세팅
	poison[0:3] = array[0:3]
	queue.append(0)
	queue.append(1)
	queue.append(2)
	#연산 시작
	while len(queue) > 0:
		idx = queue.popleft()
		current = poison[idx]
		for i in range(1,4):
			if idx + i < howLong:
				if poison[idx+i] == -1:
					poison[idx+i] = current + array[idx+i]
					queue.append(idx+i)
				elif poison[idx+i] > current + array[idx+i]:
					poison[idx+i] = current + array[idx+i]
	#연산후결과반환
	return min(poison[-3:])

howLong = int(input())
array = [int(x) for x in input().split()]
poison = [-1] * howLong

result = lessPoison(howLong, array, poison)
print(result)
