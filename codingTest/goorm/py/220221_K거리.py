# https://level.goorm.io/exam/49057/k-%EA%B1%B0%EB%A6%AC-%EC%88%98/quiz/1


#input 내용 변수 저장
user_input = int(input())
array = [int(x) for x in input().split()]

#position에 담기는 내용은 key:[step, last position]
position = dict()
for n in range(user_input):
	if array[n] in position:
		[step, last] = position[array[n]]
		if n - last > step:
			step = n - last
		position[array[n]] = [step, n]
	else: #0부터 첫 등장까지의 거리 구하기
		position[array[n]] = [n+1, n]

#리턴할 값들 용 변수 생성
K = 0
Kvalue = 0
#각 수마다의 거리(step)를 비교해 변수 저장
for k,v in position.items():
	#마지막 등장부터 배열 끝까지의 거리 구하기
	step = v[0] if user_input - v[1] < v[0] else user_input - v[1]
	if Kvalue == 0:
		K = k
		Kvalue = step
	elif Kvalue >= step:  #K값이 같으면 큰 수 출력을 위해 = 추가
		K = k
		Kvalue = step

#값 출력
print(K, Kvalue, sep=' ')
