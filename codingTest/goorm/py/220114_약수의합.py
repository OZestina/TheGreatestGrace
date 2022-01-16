# https://level.goorm.io/exam/43232/%EC%95%BD%EC%88%98%EC%9D%98-%ED%95%A9/quiz/1

user_input = int(input())
answer = user_input
for i in range(1, user_input//2+1):
	if user_input % i == 0:
		answer += i
print(answer)
