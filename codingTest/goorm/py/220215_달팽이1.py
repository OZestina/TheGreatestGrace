# https://level.goorm.io/exam/43180/%EB%8B%AC%ED%8C%BD%EC%9D%B4-1/quiz/1

# 쉬운 문제였는데 문제를 잘못 읽어서 뺑뺑 돌았다
# 문제를 제대로 이해하고 코드를 짭시다!
def snail(H, U, D, F):
	if U >= H:
		return 'Success 1'
	
	height = U
	day = 1
	STRESS = U * F/100
	
	while True:
		U -= STRESS
		height += U - D
		day += 1
		if height >= H:
			return 'Success ' + str(day)
		elif height < 0:
			return 'Failure ' + str(day-1)

[H, U, D, F] = [int(x) for x in input().split()]
print(snail(H, U, D, F))
