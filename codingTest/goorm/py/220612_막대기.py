# https://level.goorm.io/exam/48193/%EB%A7%89%EB%8C%80%EA%B8%B0/quiz/1

pole = int(input())

poles = []
for i in range(pole):
	poles.append(int(input()))

watch = poles[pole - 1]
count = 1
for i in range(pole - 2, -1, -1):
	if poles[i] > watch:
		watch = poles[i]
		count += 1
		
print(count)
