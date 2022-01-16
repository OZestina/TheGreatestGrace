# https://level.goorm.io/exam/43275/%EC%99%84%EC%A0%84%EC%88%98/quiz/1

perfectNum = [6, 28, 496, 8128]
[A, B] = [int(x) for x in input().split()]
for num in perfectNum:
	if A <= num and num <= B:
		print(num ,end=' ')
