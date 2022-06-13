# https://level.goorm.io/exam/49088/%EC%9D%98%EC%A2%8B%EC%9D%80-%ED%98%95%EC%A0%9C/quiz/1

jin, sun = [int(i) for i in input().split()]
days = int(input())

for i in range(days):
	if i % 2 == 0:
		temp = jin - int(jin / 2)
		jin -= temp
		sun += temp
	else:
		temp = sun - int(sun / 2)
		jin += temp
		sun -= temp

print(jin, sun)
