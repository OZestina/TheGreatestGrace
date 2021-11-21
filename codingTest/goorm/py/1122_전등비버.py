#https://level.goorm.io/exam/51584/%EA%B5%AC%EB%A6%84-%EA%B2%8C%EC%9E%841-%EB%AF%B8%EC%99%84%EC%84%B1/quiz/1

#1st try
#5,8번 runtime error (제한시간 1초)
[N,M] = [int(x) for x in input().split(" ")]
lamp = []
for i in range(N):
	lamp.append([int(x) for x in input().split(" ")])
	
times = int(input())
for i in range(times):
	[direction,line] = [int(x) for x in input().split(" ")]
	if direction:	#세로일 경우
		for j in range(N):
			lamp[j][line-1] += 1
	else:	#가로일 경우
		for j in range(M):
			lamp[line-1][j] += 1
				
for i in range(N):
	for j in range(M):
		print(lamp[i][j] % 2, end = " ")
	print()

	
#2nd try
#중복되는 입력값 빼주기
#그래도 5,8번 runtime error (제한시간 1초)
[N,M] = [int(x) for x in input().split(" ")]
lamp = []
for i in range(N):
	lamp.append([int(x) for x in input().split(" ")])
	
onoff = []
times = int(input())
for i in range(times):
	[direction,line] = [int(x) for x in input().split(" ")]
	if [direction,line] in onoff:
		onoff.remove([direction,line])
	else:
		onoff.append([direction,line])

for i in onoff:
	if i[0]:	#세로일 경우
		for j in range(N):
			lamp[j][i[1]-1] += 1
	else:	#가로일 경우
		for j in range(M):
			lamp[i[1]-1][j] += 1
				
for i in range(N):
	for j in range(M):
		print(lamp[i][j] % 2, end = " ")
	print()


#3rd try
#배열대신 딕셔너리써보기
#그래도 5,8번 runtime error (제한시간 1초)

[N,M] = [int(x) for x in input().split(" ")]
lamp = dict()
for i in range(N):
	temp = [int(x) for x in input().split(" ")]
	for j in range(M):
		lamp[i*M+j] = temp[j]

times = int(input())
for i in range(times):
	[direction,line] = [int(x) for x in input().split(" ")]
	if direction:	#세로일 경우
		for j in range(N):
			lamp[j*M+line-1] += 1
	else:	#가로일 경우
		for j in range(M):
			lamp[(line-1)*N+j] += 1
				
for i in range(N):
	for j in range(M):
		print(lamp[i*M + j] % 2, end = " ")
	print()
