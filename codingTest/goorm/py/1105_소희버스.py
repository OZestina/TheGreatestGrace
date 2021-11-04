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
