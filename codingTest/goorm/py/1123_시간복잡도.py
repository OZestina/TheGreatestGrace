# https://level.goorm.io/exam/49098/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84/quiz/1

#1st try
#5만 카운트해서 출력하는 방식 사용 (2*5 = 10이고, 2는 5보다 당연히 많을거니까)
#수가 커지면 시간초과로 에러 발생
def howManyZeros(n):
	if n < 5:
		return 0
	count5 = 0
	count10 = 0
	for i in range(5, n+1, 5):
		while i%5 == 0:
			count5 += 1
			i = i//5
	return count5

factorial = int(input())
print(howManyZeros(factorial))
