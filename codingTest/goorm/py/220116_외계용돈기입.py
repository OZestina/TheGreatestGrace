# https://level.goorm.io/exam/49111/%EC%99%B8%EA%B3%84%EC%9D%B8%EA%B3%BC-%EC%9A%A9%EB%8F%88%EA%B8%B0%EC%9E%85%EC%9E%A5/quiz/1

# 1st try
# 하나하나 실행하는 아주 기본적인 방법. 5~9번 time out 발생
[N, M] = [int(x) for x in input().split()]
difference = [int(x) for x in input().replace('+','').split()] #N개
for _ in range(M):	#M번 반복
	[start, end] = [int(x) for x in input().split()]
	answer = sum(difference[start-1:end]) #혹은 10~12 line
#   money = 0
# 	for day in range(start-1, end):
# 		money += difference[day]
	if money > 0: print('+',money, sep='')
	else: print(money)
    
# 2nd try
# 누적값 accumulation 리스트를 생성해 sum(1~end)-sum(1~start)의 값을 연산
# itertools의 accumulate 내장함수를 사용하면 누적값을 짧게 구할 수 있다 (line 26~28을 line 25로 대체)

from itertools import accumulate

[N, M] = [int(x) for x in input().split()]
difference = [int(x) for x in input().split()] #N개

accumulation = list(accumulate(difference))
# accumulation = [difference[0]]
# for i in range(1, N):
# 	accumulation.append(accumulation[i-1] + difference[i])

for _ in range(M):
	[start, end] = [int(x) for x in input().split()]
	if start > 1:
		answer = accumulation[end-1] - accumulation[start-2]
	else:
		answer = accumulation[end-1]
	if answer > 0: print('+',answer,sep='')
	else: print(answer)
		
    
    
# 2-2 try
# 누적값 accumulation 리스트를 생성할 때 sum으로 하면 6~9번 time out 발생
[N, M] = [int(x) for x in input().split()]
difference = [int(x) for x in input().split()] 
accumulation = [sum(difference[0:i]) for i in range(1,N+1)]

for _ in range(M):
	[start, end] = [int(x) for x in input().split()]
	if start > 1:
		answer = accumulation[end-1] - accumulation[start-2]
	else:
		answer = accumulation[end-1]
	if answer > 0: print('+',answer,sep='')
	else: print(answer)
