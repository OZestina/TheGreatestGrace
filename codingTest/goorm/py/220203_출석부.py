# https://level.goorm.io/exam/49069/%EC%B6%9C%EC%84%9D%EB%B6%80/quiz/1

name = input()
for idx in range(0,len(name)-1):
	if ord(name[idx]) > ord(name[idx+1]):
		print(name[:idx]+name[idx+1:])
		break
else:
	print(name[:len(name)-1])
