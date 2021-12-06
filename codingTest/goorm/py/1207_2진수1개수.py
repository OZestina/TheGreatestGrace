# https://level.goorm.io/exam/43100/2%EC%A7%84%EC%88%98%EC%9D%98-1-%EA%B0%9C%EC%88%98/quiz/1

def count1(n):
	n = int(n)
	binaryN = str(bin(n))
	result = binaryN.count('1')
	return result

user_input = input()
print(count1(user_input))
