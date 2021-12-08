# https://level.goorm.io/exam/43168/%EC%95%94%ED%98%B8%EC%9D%98-%EA%B0%9C%EC%88%98/quiz/1

[a,b,n] = [int(x) for x in input().split()]

if a == b:
	print(n**a)
else:
	result = 0
	for i in range(a,b+1):
		result += n**i
	print(result)
