#https://level.goorm.io/exam/49107/%EC%86%8C%ED%9D%AC%EC%99%80-%EB%B2%84%EC%8A%A4/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = list(map(lambda x: int(x), input().split(" ")))
buses = user_input[0]
atTime = user_input[1]

#버스 대수 길이의 배열 생성 (소희가 탈 수 있는 각 버스의 도착 시간 저장)
schedule = list(range(buses))

#소희가 탈 수 있는 각 버스의 도착 시간 저장
for i in range(buses):
	busInput = list(map(lambda x: int(x), input().split(" ")))
	while busInput[0] < atTime:
		busInput[0] += busInput[1]
	schedule[i] = busInput[0]

#버스 도착시간 중 가장 빠르고 번호가 낮은 버스 출력
idx = 0;
for i in range(buses):
	if (schedule[idx] > schedule[i]):
		idx = i
print(idx+1)



# 2nd try ================================================================
# 입력 for문을 돌리면서 한 번에 버스 오는 시간도 계산하도록 변경
# n(buses)만큼 연산 줄어듦

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = list(map(lambda x: int(x), input().split(" ")))
buses = user_input[0]
atTime = user_input[1]

#소희가 탈 버스 번호(-1), 타는 버스 시간을 첫번째 버스 기준으로 초기화
busInput = list(map(lambda x: int(x), input().split(" ")))
while busInput[0] < atTime:
	busInput[0] += busInput[1]
busTime = busInput[0]
idx = 1

#소희가 탈 수 있는 각 버스의 도착 시간 확인해 및 가장 빨리 도착하는 버스번호 및 시간 업데이트
for i in range(2, buses+1):
	busInput = list(map(lambda x: int(x), input().split(" ")))
	while busInput[0] < atTime:
		busInput[0] += busInput[1]
	if busTime > busInput[0]:
		busTime = busInput[0]
		idx = i

#가장 빠른 버스 번호 출력
print(idx)
