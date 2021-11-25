# https://level.goorm.io/exam/43082/%EC%B5%9C%EB%8B%A8-%EA%B1%B0%EB%A6%AC-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1
# level2 인줄 알고 시작했는데, 알고보니 레벨5...
# 어떻게 시작 해야할 지 감도 안잡힌다 (2021.11.24)

# 코딩요정님의 어-썸한 설명을 듣고 풀었다
# 1) 도착점에 도달할때까지의 여러 갈래의 방법이 있어서 BSF(breadth search first) 방식으로 진행
# 2) 각 칸까지의 최단거리를 저장하는 n*n 배열 생성
# 3) 검사할 좌표를 넣어둘 queue 생성
# 4) 가장 먼저 n-1 * n-1에 적히는 수가 최단거리 (BSF 방식이므로)

from collections import deque

square = int(input())
array = []
for _ in range(square):
	array.append([int(x) for x in input().split(" ")])

distance = [[0]*square for _ in range(square)]
queue = deque([])

if array[0][0] == 1:
	queue.append([0,0])
	distance[0][0] = 1
	
while len(queue) > 0:
	[m,n] = queue.pop()
	# print(distance)
	#0 ~ square-1	좌표만 취급...
	if m-1 > -1:
		if array[m-1][n] == 1 and distance[m-1][n] == 0:
			distance[m-1][n] = distance[m][n] + 1
			queue.append([m-1,n])
	if n-1 > -1:
		if array[m][n-1] == 1 and distance[m][n-1] == 0:
			distance[m][n-1] = distance[m][n] + 1
			queue.append([m,n-1])
	if m+1 < square:
		if array[m+1][n] == 1 and distance[m+1][n] == 0:
			distance[m+1][n] = distance[m][n] + 1
			queue.append([m+1,n])
			if m+1 == n == square-1:
				print(distance[m+1][n])
				break
	if n+1 < square:
		if array[m][n+1] == 1 and distance[m][n+1] == 0:
			distance[m][n+1] = distance[m][n] + 1
			queue.append([m,n+1])
			if n+1 == m == square-1:
				print(distance[m][n+1])
				break
	
